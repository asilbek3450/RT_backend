from rest_framework.serializers import ModelSerializer

from connections.models import BookTest, UserTest, Order


class BookTestSerializer(ModelSerializer):
    class Meta:
        model = BookTest
        fields = '__all__'
        
        read_only_fields = ['id']
        
        depth = 1


class BookTestCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = BookTest
        fields = [
            'id',
            'book_id',
            'test_id',
        ]
        
        read_only_fields = ['id']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['book_id'] = instance.book_id.title
        representation['test_id'] = instance.test_id.title
        return representation


class UserTestSerializer(ModelSerializer):
    class Meta:
        model = UserTest
        fields = '__all__'
        
        read_only_fields = ['id']
        
        depth = 1
    
    
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
