from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'siteidentity', views.SiteIdentityViewSet)
router.register(r'navigationitem', views.NavigationItemViewSet)
router.register(r'footerinfo', views.FooterInfoViewSet)
router.register(r'footerquicklink', views.FooterQuickLinkViewSet)
router.register(r'footercontact', views.FooterContactViewSet)
router.register(r'sociallink', views.SocialLinkViewSet)

urlpatterns = [ path('', include(router.urls)) ]
