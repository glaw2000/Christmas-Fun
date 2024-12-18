from . import views
from django.urls import path
from .views import HomePage, Coal, NaughtyNice

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('coal/', Coal.as_view(), name='coal'),
    path('naughty_nice/', NaughtyNice.as_view(), name='naughty_nice'),
]