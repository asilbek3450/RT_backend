from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import AnswerPictureSerializer, AnswerSerializer, TestPictureSerializer, ClassesSerializer, \
    ThemesSerializer, TestTypeSerializer, TestSerializer, TestCreateUpdateSerializer
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


class TestView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'question']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TestCreateUpdateSerializer
        return super().get_serializer_class()


class TestRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
