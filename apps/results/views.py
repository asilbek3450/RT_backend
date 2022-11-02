from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from results.models import Result
from results.serializers import ResultSerializer


# Create your views here.
class ResultListCreateView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'user_id', 'order_id', 'answer_id', 'question_id']


class ResultRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
