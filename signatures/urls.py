from django.conf.urls import url
from viewsets import *
from . import views

from rest_framework import routers
# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'player', PlayerViewSet, r"player")


urlpatterns = [

    # REST API root view (generated by DRF router)
    url(r'^api/', include(router.urls, namespace='api')),


    url(r'^$', views.testview, name='index'),
]
