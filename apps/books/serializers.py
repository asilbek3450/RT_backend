from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from books.models import Book, Science, BookType


class BookSerializer(ModelSerializer):
    science_1 = CharField(source='science1.title')
    science_2 = CharField(source='science2.title')

    class Meta:
        model = Book
        fields = ('id', 'science_1', 'science_2', 'language_id', 'book_type', 'is_free')


class ScienceSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'


class BookTypeSerializer(ModelSerializer):
    class Meta:
        model = BookType
        fields = ('id', 'title')
