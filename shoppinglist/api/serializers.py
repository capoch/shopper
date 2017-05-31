from rest_framework.serializers import ModelSerializer

from shoppinglist.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'description', 'amount', 'private', 'image',
        'due_date', 'pending', 'created', 'created_by', 'updated', 'updated_by', 'finalized',
        'finalized_by']
