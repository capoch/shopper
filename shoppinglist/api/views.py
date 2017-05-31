from rest_framework.generics import ListAPIView

from shoppinglist.models import Item
from .serializers import ItemSerializer

class ItemListAPIView(ListAPIView):
    def get(self, request):
        queryset = Item.objects.filter(pending=True, private=False) | Item.objects.filter(pending=True, private=True, created_by=request.user)
        serializer_class = ItemSerializer
        print("house")
