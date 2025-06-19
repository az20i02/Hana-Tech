from rest_framework import viewsets
from .models import *
from .serializers import *

class WorkIntroViewSet(viewsets.ModelViewSet):
    queryset = WorkIntro.objects.all()
    serializer_class = WorkIntroSerializer

class WorkImpactOverviewViewSet(viewsets.ModelViewSet):
    queryset = WorkImpactOverview.objects.all()
    serializer_class = WorkImpactOverviewSerializer

class WorkImpactStatViewSet(viewsets.ModelViewSet):
    queryset = WorkImpactStat.objects.all()
    serializer_class = WorkImpactStatSerializer

class FeaturedProjectViewSet(viewsets.ModelViewSet):
    queryset = FeaturedProject.objects.all()
    serializer_class = FeaturedProjectSerializer

class ProjectHighlightViewSet(viewsets.ModelViewSet):
    queryset = ProjectHighlight.objects.all()
    serializer_class = ProjectHighlightSerializer

class EducationalResourceViewSet(viewsets.ModelViewSet):
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer
