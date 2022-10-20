from django.db import models


class AnswerPicture(models.Model):
    image = models.ImageField(upload_to='answer_pictures')

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-id']


class Answers(models.Model):
    answer = models.CharField(max_length=150, blank=True)
    picture_id = models.ForeignKey("tests.AnswerPicture", on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.answer)