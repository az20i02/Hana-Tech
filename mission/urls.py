from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'missionintro', views.MissionIntroViewSet)
router.register(r'vision', views.VisionViewSet)
router.register(r'value', views.ValueViewSet)
router.register(r'approach', views.ApproachViewSet)
router.register(r'approachpillar', views.ApproachPillarViewSet)

urlpatterns = [ path('', include(router.urls)) ]
