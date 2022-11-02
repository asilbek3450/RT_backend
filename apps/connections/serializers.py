from rest_framework.serializers import ModelSerializer

from connections.models import BookTest, UserTest, Order


class BookTestSerializer(ModelSerializer):
    class Meta:
        model = BookTest
        fields = '__all__'


class UserTestSerializer(ModelSerializer):
    class Meta:
        model = UserTest
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

