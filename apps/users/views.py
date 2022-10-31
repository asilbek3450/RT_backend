from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView

from users.models import User, LanguageChoices
from users.serializers import UserSerializer, LanguageChoiceSerializer


# Create your views here.
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'full_name', 'phone_number']


class LanguageChoiceListCreateView(ListCreateAPIView):
    queryset = LanguageChoices.objects.all()
    serializer_class = LanguageChoiceSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']


class HumanTypeListCreateView(ListCreateAPIView):
    queryset = LanguageChoices.objects.all()
    serializer_class = LanguageChoiceSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']
