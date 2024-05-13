from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet , GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename="user")
router.register(r'groups',GroupViewSet,basename="group")

app_name = 'quickstart'
urlpatterns = [
    path('', include(router.urls)),
]
