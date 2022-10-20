from django.contrib import admin
from tests.models.test import Test
from tests.models.answer import Answers, AnswerPicture
# Register your models here.

admin.site.register(Test)
admin.site.register(Answers)
admin.site.register(AnswerPicture)

