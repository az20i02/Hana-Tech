from rest_framework import viewsets
from .models import *
from .serializers import *

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class MissionSectionViewSet(viewsets.ModelViewSet):
    queryset = MissionSection.objects.all()
    serializer_class = MissionSectionSerializer

class ImpactSectionViewSet(viewsets.ModelViewSet):
    queryset = ImpactSection.objects.all()
    serializer_class = ImpactSectionSerializer

class ImpactStatViewSet(viewsets.ModelViewSet):
    queryset = ImpactStat.objects.all()
    serializer_class = ImpactStatSerializer

class ImpactHighlightViewSet(viewsets.ModelViewSet):
    queryset = ImpactHighlight.objects.all()
    serializer_class = ImpactHighlightSerializer
