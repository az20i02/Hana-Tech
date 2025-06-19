from rest_framework import viewsets
from .models import *
from .serializers import *

class SiteIdentityViewSet(viewsets.ModelViewSet):
    queryset = SiteIdentity.objects.all()
    serializer_class = SiteIdentitySerializer

class NavigationItemViewSet(viewsets.ModelViewSet):
    queryset = NavigationItem.objects.all()
    serializer_class = NavigationItemSerializer

class FooterInfoViewSet(viewsets.ModelViewSet):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer

class FooterQuickLinkViewSet(viewsets.ModelViewSet):
    queryset = FooterQuickLink.objects.all()
    serializer_class = FooterQuickLinkSerializer

class FooterContactViewSet(viewsets.ModelViewSet):
    queryset = FooterContact.objects.all()
    serializer_class = FooterContactSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
