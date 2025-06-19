from rest_framework import serializers
from .models import *

class AboutIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutIntro
        fields = '__all__'

class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class AboutValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutValue
        fields = '__all__'

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'
