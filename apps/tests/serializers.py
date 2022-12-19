from rest_framework.serializers import ModelSerializer

from tests.models import Test, TestType, AnswerPicture, Answer, Themes, Classes, TestPicture


class AnswerPictureSerializer(ModelSerializer):
    class Meta:
        model = AnswerPicture
        fields = ['id', 'image']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

        depth = 1


class TestPictureSerializer(ModelSerializer):
    class Meta:
        model = TestPicture
        fields = ['id', 'image']


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

        depth = 1


class TestCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['classes'] = instance.classes.title
        representation['themes'] = instance.themes.title
        representation['test_type'] = instance.test_type.title
        return representation
