from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'herosection', views.HeroSectionViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'missionsection', views.MissionSectionViewSet)
router.register(r'impactsection', views.ImpactSectionViewSet)
router.register(r'impactstat', views.ImpactStatViewSet)
router.register(r'impacthighlight', views.ImpactHighlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
