from abc import ABC

from rest_framework.serializers import ModelSerializer

from users.models import User, LanguageChoices, HumanType


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LanguageChoiceSerializer(ModelSerializer):
    class Meta:
        model = LanguageChoices
        fields = '__all__'


class HumanTypeSerializer(ModelSerializer):
    class Meta:
        model = HumanType
        fields = '__all__'
