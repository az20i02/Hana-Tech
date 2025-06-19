from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'aboutintro', views.AboutIntroViewSet)
router.register(r'ourstory', views.OurStoryViewSet)
router.register(r'teammember', views.TeamMemberViewSet)
router.register(r'aboutvalue', views.AboutValueViewSet)
router.register(r'contactinformation', views.ContactInformationViewSet)

urlpatterns = [ path('', include(router.urls)) ]
