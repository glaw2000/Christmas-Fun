from django.urls import path
from .views import nice_list_view, wish_list_view

urlpatterns = [
    path('', views.NiceList.as_view(), name='nice_list'),
    path('wishlist/<int:pk>', views.wish_list, name='wishes'),
    path('<int:pk>/coal/', views.coal_wisher, name='coal_detail'),
]

