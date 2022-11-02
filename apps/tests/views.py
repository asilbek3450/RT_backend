from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import AnswerPictureSerializer, AnswerSerializer, TestPictureSerializer, ClassesSerializer, \
    ThemesSerializer, TestTypeSerializer, TestSerializer
from tests.models import Answer, AnswerPicture, TestPicture, Classes, Themes, TestType, Test


# Create your views here.


class AnswerPictureView(ListCreateAPIView):
    queryset = AnswerPicture.objects.all()
    serializer_class = AnswerPictureSerializer


class AnswerView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'answer']


class TestPictureView(ListCreateAPIView):
    queryset = TestPicture.objects.all()
    serializer_class = TestPictureSerializer


class ClassesView(ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class ThemesView(ListCreateAPIView):
    queryset = Themes.objects.all()
    serializer_class = ThemesSerializer


class TestTypeView(ListCreateAPIView):
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer


class TestView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'question']


class TestRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
