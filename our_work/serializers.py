from rest_framework import serializers
from .models import *

class WorkIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkIntro
        fields = '__all__'

class WorkImpactOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImpactOverview
        fields = '__all__'

class WorkImpactStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImpactStat
        fields = '__all__'

class FeaturedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedProject
        fields = '__all__'

class ProjectHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectHighlight
        fields = '__all__'

class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResource
        fields = '__all__'
