from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView
    )
from shoppinglist.models import Item
from .serializers import ItemSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class ItemList(ListCreateAPIView):
    # queryset = Item.objects.filter(pending=True)
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated = None)

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(pending=True, private = False) | Item.objects.filter(pending=True, private = True, created_by = self.request.user)

class ItemArchive(ListAPIView):
    # queryset = Item.objects.filter(pending=True)
    today = timezone.now().date()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(pending=False, finalized__lte=timezone.now().date(),
        private=False) | Item.objects.filter(pending=False, finalized__lte=timezone.now().date(),
        private = True, created_by = self.request.user)


class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated=timezone.now().date())


class ItemBuy(UpdateAPIView):

    queryset = Item.objects.filter(pending=True, finalized = None, finalized_by = None)
    serializer_class = ItemSerializer
    #permission noch korrigieren oder okay?
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(finalized_by=self.request.user, finalized=timezone.now().date(), pending=False)

class ItemReactivate(UpdateAPIView):

    serializer_class = ItemSerializer
    #permission noch korrigieren oder okay?
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(pending=False, finalized__lte=timezone.now().date(),
        private=False) | Item.objects.filter(pending=False, finalized__lte=timezone.now().date(),
        private = True, created_by = self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated=timezone.now().date(), finalized_by=None, finalized=None, pending=True)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
