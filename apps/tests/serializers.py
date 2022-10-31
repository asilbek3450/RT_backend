from rest_framework.serializers import ModelSerializer

from tests.models import Test, TestType, AnswerPicture, Answer, Themes, Classes, TestPicture


class AnswerPictureSerializer(ModelSerializer):
    class Meta:
        model = AnswerPicture
        fields = ('id', 'image')


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class TestPictureSerializer(ModelSerializer):
    class Meta:
        model = TestPicture
        fields = ('id', 'image')


class ClassesSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class ThemesSerializer(ModelSerializer):
    class Meta:
        model = Themes
        fields = '__all__'


class TestTypeSerializer(ModelSerializer):
    class Meta:
        model = TestType
        fields = '__all__'


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
