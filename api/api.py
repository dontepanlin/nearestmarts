from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import Group


from .serializers import UserSerializer, PlaceSerializer, CategorySerializer, ItemSerializer, PiarSerializer
from .models import User, Item, Place, Category, Piar

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()

class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, 'required_groups', {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups.
        return all([is_in_group(request.user, group_name) for group_name in required_groups])


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
        permissions.IsAuthenticatedOrReadOnly
    ]

class UserPlaceList(generics.ListAPIView):
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(UserPlaceList, self).get_queryset()
        return queryset.filter(user__pk=self.kwargs.get('pk'))

class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = StandardResultsSetPagination
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
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(PlaceItemList, self).get_queryset()
        return queryset.filter(place__id=self.kwargs.get('pk'))

class CategoryItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(CategoryItemList, self).get_queryset()
        return queryset.filter(category__id=self.kwargs.get('pk'))

class CategoryPlaceList(generics.ListAPIView):
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(CategoryPlaceList, self).get_queryset()
        return queryset.filter(categories__id=self.kwargs.get('pk'))

class PiarList(generics.ListCreateAPIView):
    model = Piar
    serializer_class = PiarSerializer
    queryset = Piar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]