from django.conf.urls import include, url

from .views import show_cats

from .api import PlaceList, PlaceDetail, UserPlaceList
from .api import CategoryList
from .api import ItemList, ItemDetail, PlaceItemList, CategoryItemList, CategoryPlaceList
from .api import PiarList

place_urls = [
    url(r'^(?P<pk>\d+)/items$', PlaceItemList.as_view(), name='placeitem-list'),
    url(r'^(?P<pk>\d+)$', PlaceDetail.as_view(), name='place-detail'),
    url(r'^$', PlaceList.as_view(), name='place-list')
]

item_urls = [
    url(r'^(?P<pk>\d+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^$', ItemList.as_view(), name='item-list')
]

urlpatterns = [
    url(r'^users/', include('rest_auth.urls')),
    url(r'^users/user/(?P<username>[0-9a-zA-Z_-]+)/places$', UserPlaceList.as_view(), name='userplace-list'),
    url(r'^users/registration/', include('rest_auth.registration.urls')),
    url(r'^cats/$', view=show_cats),
    url(r'^categories/$', CategoryList.as_view(), name='categories-list'),
    url(r'^categories/(?P<pk>\d+)/items', CategoryItemList.as_view(), name='categoryitem-list'),
    url(r'^categories/(?P<pk>\d+)/places', CategoryPlaceList.as_view(), name='categoryplace-list'),
    url(r'^places/', include(place_urls)),
    url(r'^items/', include(item_urls)),
    url(r'^piars/', PiarList.as_view(), name='piar-list'),
]