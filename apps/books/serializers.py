from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from books.models import Book, Science, BookType


class ScienceSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'

        read_only_fields = ['id']


class BookTypeSerializer(ModelSerializer):
    class Meta:
        model = BookType
        fields = ('id', 'title')

        read_only_fields = ['id']


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'science1', 'science2', 'language_id', 'book_type', 'is_free')

        read_only_fields = ['id']

        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['science1'] = instance.science1.title
        representation['science2'] = instance.science2.title
        return representation


class BookCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'science1',
            'science2',
            'language_id',
            'book_type',
            'is_free',
        ]

        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['science1'] = instance.science1.title
        representation['science2'] = instance.science2.title
        return representation
