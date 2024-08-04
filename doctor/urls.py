from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter() #router
from .import views



router.register('list', views.DoctorViewset,) #router ar antana
router.register('specialization', views.SpecializationViewset,) #router ar antana
router.register('designation', views.DesignationViewset,) #router ar antana
router.register('reviews', views.ReviewViewset,) #router ar antana
router.register('available_time', views.AvailableTimeViewset,) #router ar antana
urlpatterns = [
    path('', include(router.urls)),
]