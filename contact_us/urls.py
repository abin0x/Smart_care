from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .import views



router.register('', views.ContactusViewset,)
urlpatterns = [
    path('', include(router.urls)),
]