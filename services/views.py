from rest_framework import viewsets
from .models import *
from .serializers import *

class ServicesIntroViewSet(viewsets.ModelViewSet):
    queryset = ServicesIntro.objects.all()
    serializer_class = ServicesIntroSerializer

class WorkshopSectionViewSet(viewsets.ModelViewSet):
    queryset = WorkshopSection.objects.all()
    serializer_class = WorkshopSectionSerializer

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer

class LegalSupportSectionViewSet(viewsets.ModelViewSet):
    queryset = LegalSupportSection.objects.all()
    serializer_class = LegalSupportSectionSerializer

class LegalServiceViewSet(viewsets.ModelViewSet):
    queryset = LegalService.objects.all()
    serializer_class = LegalServiceSerializer

class LegalSupportContactViewSet(viewsets.ModelViewSet):
    queryset = LegalSupportContact.objects.all()
    serializer_class = LegalSupportContactSerializer

class CommunitySupportSectionViewSet(viewsets.ModelViewSet):
    queryset = CommunitySupportSection.objects.all()
    serializer_class = CommunitySupportSectionSerializer

class CommunityInitiativeViewSet(viewsets.ModelViewSet):
    queryset = CommunityInitiative.objects.all()
    serializer_class = CommunityInitiativeSerializer
