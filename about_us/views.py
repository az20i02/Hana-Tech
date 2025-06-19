from rest_framework import viewsets
from .models import *
from .serializers import *

class AboutIntroViewSet(viewsets.ModelViewSet):
    queryset = AboutIntro.objects.all()
    serializer_class = AboutIntroSerializer

class OurStoryViewSet(viewsets.ModelViewSet):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class AboutValueViewSet(viewsets.ModelViewSet):
    queryset = AboutValue.objects.all()
    serializer_class = AboutValueSerializer

class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer
