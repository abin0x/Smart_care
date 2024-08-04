from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter() #router
from .import views



router.register('', views.ServiceViewset,) #router ar antana
urlpatterns = [
    path('', include(router.urls)),
]