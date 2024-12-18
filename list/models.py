from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WishList(models.Model):
    """

    """
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wisher")
    wish_item = models.JSONField(default=list)

    def __str__(self):
        wishes = self.wish_item if isinstance(self.wish_item, list) else []
        return f"{self.fk_user_id}'s wishes: {', '.join(wishes[:3])}"
    


class Coal(models.Model):
    """
    Stores a coal relationship between Wish List ID and User Id.
    """
    fk_wish_list_id = models.ForeignKey(
        WishList, on_delete=models.CASCADE, related_name="coals")
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="coaler")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('fk_wish_list_id', 'fk_user_id')

    def __str__(self):
        return f"{self.fk_user_id} coaled {self.fk_wish_list_id}"

    def total_coals(self):
        return self.total_coals.count()