from django.db import models

from books.models import Science
from users.models import User, LanguageChoices, HumanType


class AnswerPicture(models.Model):
    image = models.ImageField(upload_to='answer_pictures')

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-id']


class Answer(models.Model):
    answer = models.CharField(max_length=150, blank=True)
    picture_id = models.ForeignKey(AnswerPicture, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.answer if self.answer else self.picture_id)


class TestPicture(models.Model):
    image = models.ImageField(upload_to='test_pictures')

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-id']


class Classes(models.Model):
    title = models.CharField(max_length=45, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Themes(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True)
    science_id = models.ForeignKey(Science, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.name)


class TestType(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Test(models.Model):
    question = models.TextField(blank=True)
    answer_id = models.ManyToManyField(Answer, blank=True)
    is_visible = models.BooleanField(default=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    picture_id = models.ForeignKey(TestPicture, on_delete=models.CASCADE, null=True, blank=True)
    language_id = models.ForeignKey(LanguageChoices, on_delete=models.CASCADE, null=True, blank=True)
    theme_id = models.ForeignKey(Themes, on_delete=models.CASCADE, null=True, blank=True)

    for_person_id = models.ForeignKey(HumanType, on_delete=models.CASCADE, null=True, blank=True)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
