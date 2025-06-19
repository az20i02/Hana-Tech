from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'servicesintro', views.ServicesIntroViewSet)
router.register(r'workshopsection', views.WorkshopSectionViewSet)
router.register(r'workshop', views.WorkshopViewSet)
router.register(r'legalsupportsection', views.LegalSupportSectionViewSet)
router.register(r'legalservice', views.LegalServiceViewSet)
router.register(r'legalsupportcontact', views.LegalSupportContactViewSet)
router.register(r'communitysupportsection', views.CommunitySupportSectionViewSet)
router.register(r'communityinitiative', views.CommunityInitiativeViewSet)

urlpatterns = [ path('', include(router.urls)) ]
