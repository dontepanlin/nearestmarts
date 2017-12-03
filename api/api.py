from rest_framework import generics, permissions


from .serializers import UserSerializer, PlaceSerializer, CategorySerializer, ItemSerializer
from .models import User, Item, Place, Category


class PlaceList(generics.ListCreateAPIView):
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class UserPlaceList(generics.ListAPIView):
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def get_queryset(self):
        queryset = super(UserPlaceList, self).get_queryset()
        return queryset.filter(user__username=self.kwargs.get('username'))

class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class ItemList(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class PlaceItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        queryset = super(PlaceItemList, self).get_queryset()
        return queryset.filter(place__id=self.kwargs.get('pk'))

class CategoryItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        queryset = super(CategoryItemList, self).get_queryset()
        return queryset.filter(category__id=self.kwargs.get('pk'))