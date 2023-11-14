from django.db import models
from django.contrib.auth.models import User


class GearList(models.Model):
    """
    Gear list model related to a User instance
    categories are set with default category and image
    """
    OTHER = 'other'
    BIKE = 'bike'
    CLIMBING = 'climbing'
    HIKING = 'hiking'

    GEAR_LIST_CATEGORIES = [
        (OTHER, 'Other'),
        (BIKE, 'Bike'),
        (CLIMBING, 'Climbing'),
        (HIKING, 'Hiking'),
    ]

    category = models.CharField(
        max_length=20, choices=GEAR_LIST_CATEGORIES, default=OTHER)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../other_ustsrk.jpg', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):

        return f'{self.id} {self.title}'
