from rest_framework import serializers
from .models import *

class SiteIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteIdentity
        fields = '__all__'

class NavigationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationItem
        fields = '__all__'

class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterInfo
        fields = '__all__'

class FooterQuickLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterQuickLink
        fields = '__all__'

class FooterContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterContact
        fields = '__all__'

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
