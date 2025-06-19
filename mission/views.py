from rest_framework import viewsets
from .models import *
from .serializers import *

class MissionIntroViewSet(viewsets.ModelViewSet):
    queryset = MissionIntro.objects.all()
    serializer_class = MissionIntroSerializer

class VisionViewSet(viewsets.ModelViewSet):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class ApproachViewSet(viewsets.ModelViewSet):
    queryset = Approach.objects.all()
    serializer_class = ApproachSerializer

class ApproachPillarViewSet(viewsets.ModelViewSet):
    queryset = ApproachPillar.objects.all()
    serializer_class = ApproachPillarSerializer
