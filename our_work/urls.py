from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'workintro', views.WorkIntroViewSet)
router.register(r'workimpactoverview', views.WorkImpactOverviewViewSet)
router.register(r'workimpactstat', views.WorkImpactStatViewSet)
router.register(r'featuredproject', views.FeaturedProjectViewSet)
router.register(r'projecthighlight', views.ProjectHighlightViewSet)
router.register(r'educationalresource', views.EducationalResourceViewSet)

urlpatterns = [ path('', include(router.urls)) ]
