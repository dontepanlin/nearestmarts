from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey


#
# Create your models here.
# Model User.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # custom fields for user
    type = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


#
# class Users(AbstractUser):
#     type = models.IntegerField(default=0)
#     #any other fields you want

# Модель категории
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=False)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

#   Модель торговой точки
class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='')
    lat = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    lon = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

# Модель товара
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='')
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Piar(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    poster = models.ImageField(blank=True, null=True, upload_to='posters/')
