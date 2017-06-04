from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField

from shoppinglist.models import Item

class ItemSerializer(ModelSerializer):
    created_by = ReadOnlyField(source='created_by.username')
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'description', 'amount', 'private', 'image',
        'due_date', 'pending', 'created', 'created_by', 'updated', 'updated_by', 'finalized',
        'finalized_by']

class UserSerializer(ModelSerializer):
    items = PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'items')
