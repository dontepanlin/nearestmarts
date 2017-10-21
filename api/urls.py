from django.conf.urls import include, url


urlpatterns = [
    url(r'^users/', include('rest_auth.urls')),
    url(r'^users/registration/', include('rest_auth.registration.urls'))
]