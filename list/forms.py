from django import forms


class WishItemForm(forms.Form):
    item = forms.CharField(max_length=200, label='Add a wish item')
