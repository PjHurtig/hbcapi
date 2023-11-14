from gearlists.models import GearList
from django.db import models
from django.contrib.auth.models import User


class GearItem(models.Model):
    """
    Gear items, related to user and gearlistimage has a default
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gearlist = models.ForeignKey(GearList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../gear_gw6qtj.jpg', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.about
