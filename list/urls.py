from django.urls import path
from .views import NiceList, wish_list, coal_wisher, add_wish_item

urlpatterns = [
    path('', NiceList.as_view(), name='nice_list'),
    path('wishlist/<int:pk>', wish_list, name='wishes'),
    path('<int:pk>/coal/', coal_wisher, name='coal_detail'),
    path('wishlist/<int:pk>/add/', add_wish_item, name='add_wish_item'),
]
