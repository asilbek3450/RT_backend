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
    science1 = ScienceSerializer()
    science2 = ScienceSerializer()

    class Meta:
        model = Book
        fields = ('id', 'science1', 'science2', 'language_id', 'book_type', 'is_free')

        read_only_fields = ['id']

