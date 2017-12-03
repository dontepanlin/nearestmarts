from django.test import TestCase

# Create your tests here.


from api.models import Category

rock = Category.objects.create(name="Rock")
blues = Category.objects.create(name="Blues")
Category.objects.create(name="Hard Rock", parent=rock)
Category.objects.create(name="Pop Rock", parent=rock)