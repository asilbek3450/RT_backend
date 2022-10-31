from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.models import Book, Science, BookType
from books.serializers import BookSerializer, ScienceSerializer, BookTypeSerializer


# Create your views here.


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id']


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ScienceListCreateView(ListCreateAPIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']


class BookTypeListCreateView(ListCreateAPIView):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'title']

