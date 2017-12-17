from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import Place, Category, Item


class UserSerializer(UserDetailsSerializer):
    type = serializers.IntegerField(source="userprofile.type")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('type',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        type = profile_data.get('type')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and type:
            profile.type = type
            profile.save()
        return instance

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'category', 'place', 'name', 'description', 'cost')

class PlaceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Place
        fields = ('id', 'user', 'name', 'description', 'lat', 'lon', 'items')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','parent')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True)
        return fields



