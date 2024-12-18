from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import WishList, Coal
from django.contrib.auth.models import User
from .forms import WishItemForm


class NiceList(ListView):
    """

    """
    model = User
    template_name = 'list/nice_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_active=True)


def wish_list(request, pk):
    """
    Display the wish list for a specific user
    """
    user = get_object_or_404(User, pk=pk)
    wishes = WishList.objects.filter(fk_user_id=user)
    user_has_coaled = Coal.objects.filter(
        fk_wish_list_id__in=wishes,
        fk_user_id=request.user
    ).exists() if request.user.is_authenticated else False

    total_coals = Coal.objects.filter(fk_wish_list_id__in=wishes).count()

    return render(
        request,
        "list/wish_list.html",
        {
            "wishes": wishes,
            "user_has_coaled": user_has_coaled,
            "wish_list_owner": user,
            "total_coals": total_coals,
        },
    )


@login_required
def add_wish_item(request, pk):
    user = get_object_or_404(User, pk=pk)
    wish_list, created = WishList.objects.get_or_create(fk_user_id=user)

    if request.method == 'POST':
        form = WishItemForm(request.POST)
        if form.is_valid():
            new_item = form.cleaned_data['item']
            
            # Initialize wish_item as an empty list if it's None or not a list
            if wish_list.wish_item is None or not isinstance(wish_list.wish_item, list):
                wish_list.wish_item = []

            # Append the new item
            wish_list.wish_item.append(new_item)

            # Save the updated wish list
            wish_list.save()
            messages.success(request, 'Item added to your wish list!')
            return redirect('wishes', pk=user.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WishItemForm()

    return render(request, 'list/add_wish_item.html', {'form': form, 'wish_list_owner': user})


@login_required
def coal_wisher(request, pk):
    """
    Toggles a coal icon for the entire wish list
    """
    user = get_object_or_404(User, pk=pk)
    wish_lists = WishList.objects.filter(fk_user_id=user)

    # Check if there are any wish lists for the user
    if not wish_lists.exists():
        return JsonResponse({'error': 'No wish lists found for this user.'}, status=400)

    # Use the first wish list as a representative for the entire list
    first_wish_list = wish_lists.first()

    # Get or create a Coal instance
    coal, created = Coal.objects.get_or_create(
        fk_wish_list_id=first_wish_list,
        fk_user_id=request.user
    )

    if not created:
        # If it already exists, delete all coals for this user in the user's wish lists
        Coal.objects.filter(fk_wish_list_id__in=wish_lists, fk_user_id=request.user).delete()
        coaled = False
    else:
        coaled = True

    # Count total coals for this user's wish lists
    coals_count = Coal.objects.filter(fk_wish_list_id__in=wish_lists).count()
    
    print(f"Coal count: {coals_count}")
    
    return JsonResponse({
        'coaled': coaled,
        'coal_count': coals_count
    })
