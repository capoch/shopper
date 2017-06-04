from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemList, ItemDetail, UserList, UserDetail, ItemBuy, ItemArchive, ItemReactivate

urlpatterns = [
    url(r'^items/$', ItemList.as_view()),
    url(r'^items/archive/$', ItemArchive.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', ItemDetail.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/buy/$', ItemBuy.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/reactivate/$', ItemReactivate.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = [
#     url(r'^$', ItemList.as_view(), name="home"),
#     url(r'^archive/$', item_archive, name="archive"),
#     url(r'^create/$', item_create, name="create"),
#     url(r'^(?P<id>[\w-]+)/$', item_detail, name="detail"),
#     url(r'^(?P<id>[\w-]+)/buy/$', buy_item, name="buy"),
#     url(r'^(?P<id>[\w-]+)/edit/$', item_edit, name="edit"),
#     url(r'^(?P<id>[\w-]+)/reactivate/$', reactivate_item, name="reactivate"),
# ]
