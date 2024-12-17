from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    """
    Stores user profiles related to :model: 'auth.User'
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    display_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    naughty = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    @property
    def get_display_name(self):
        return self.display_name or self.user.username