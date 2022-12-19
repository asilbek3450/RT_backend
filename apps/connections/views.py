from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from connections.models import BookTest, UserTest, Order
from connections.serializers import BookTestSerializer, UserTestSerializer, OrderSerializer, \
    BookTestCreateUpdateSerializer


# Create your views here.


class BookTestViewSet(ModelViewSet):
    queryset = BookTest.objects.all()
    serializer_class = BookTestSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'book_id', 'test_id']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookTestCreateUpdateSerializer
        return super().get_serializer_class()


class BookTestRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = BookTest.objects.all()
    serializer_class = BookTestSerializer
    

class UserTestListCreateView(RetrieveUpdateDestroyAPIView):
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
