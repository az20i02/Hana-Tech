from rest_framework import serializers
from .models import *

class ServicesIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIntro
        fields = '__all__'

class WorkshopSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopSection
        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

class LegalSupportSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalSupportSection
        fields = '__all__'

class LegalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalService
        fields = '__all__'

class LegalSupportContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalSupportContact
        fields = '__all__'

class CommunitySupportSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunitySupportSection
        fields = '__all__'

class CommunityInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityInitiative
        fields = '__all__'
