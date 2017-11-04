from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# Model User.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 1)
    birth_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#   Модель торговой точки
class Place (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = gender = models.CharField(max_length = 100)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)

# Модель категории
class Category (models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(blank=True, null=True)

# Модель товара
class Item (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = gender = models.CharField(max_length=100)
    cost = models.FloatField(blank=True, null=True)


