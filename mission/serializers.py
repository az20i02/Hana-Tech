from rest_framework import serializers
from .models import *

class MissionIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionIntro
        fields = '__all__'

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = '__all__'

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'

class ApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approach
        fields = '__all__'

class ApproachPillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproachPillar
        fields = '__all__'
