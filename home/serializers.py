from rest_framework import serializers
from .models import *

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class MissionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSection
        fields = '__all__'

class ImpactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactSection
        fields = '__all__'

class ImpactStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactStat
        fields = '__all__'

class ImpactHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactHighlight
        fields = '__all__'
