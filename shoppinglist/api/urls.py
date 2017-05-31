from django.conf.urls import url
from django.contrib import admin
from shoppinglist.api.views import ItemListAPIView

urlpatterns = [
    url(r'^$', ItemListAPIView.as_view(), name="home"),
    # url(r'^archive/$', item_archive, name="archive"),
    # url(r'^create/$', item_create, name="create"),
    # url(r'^(?P<id>[\w-]+)/$', item_detail, name="detail"),
    # url(r'^(?P<id>[\w-]+)/buy/$', buy_item, name="buy"),
    # url(r'^(?P<id>[\w-]+)/edit/$', item_edit, name="edit"),
    # url(r'^(?P<id>[\w-]+)/reactivate/$', reactivate_item, name="reactivate"),
]
