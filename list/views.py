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
    if request.method == 'POST':
        form = WishItemForm(request.POST)
        if form.is_valid():
            new_item = form.cleaned_data['item']
            wish_list,
            created = WishList.objects.get_or_create(fk_user_id=user)
            if isinstance(wish_list.wish_item, list):
                wish_list.wish_item.append(new_item)
            else:
                wish_list.wish_item = [new_item]
            wish_list.save()
            messages.success(request, 'Item added to your wish list!')
            return redirect('wishes', pk=pk)
    else:
        form = WishItemForm()

    return render(request, 'list/add_wish_item.html', {'form': form})


@login_required
def coal_wisher(request, pk):
    """
    Toggles a coal icon for the entire wish list
    """
    user = get_object_or_404(User, pk=pk)
    wish_lists = WishList.objects.filter(fk_user_id=user)

    coal, created = Coal.objects.get_or_create(
        fk_wish_list_id=wish_lists.first(),
        fk_user_id=request.user
    )
    if not created:
        Coal.objects.filter(
            fk_wish_list_id__in=wish_lists,
            fk_user_id=request.user
        ).delete()
        coaled = False
    else:
        coaled = True

    coals_count = Coal.objects.filter(fk_wish_list_id__in=wish_lists).count()
    return JsonResponse({
        'coaled': coaled,
        'coal_count': coals_count
    })
