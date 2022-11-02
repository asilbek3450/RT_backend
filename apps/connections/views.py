from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from connections.models import BookTest, UserTest, Order
from connections.serializers import BookTestSerializer, UserTestSerializer, OrderSerializer


# Create your views here.


class BookTestListCreateView(ListCreateAPIView):
    queryset = BookTest.objects.all()
    serializer_class = BookTestSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'book_id', 'test_id']


class UserTestListCreateView(ListCreateAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'user_id', 'test_id']


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'user_id', 'book_id']


class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
