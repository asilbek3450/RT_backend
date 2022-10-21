from django.contrib import admin

from .models.answer import Answers, AnswerPicture
from .models.test import Test

# Register your models here.
admin.site.register(Test)
admin.site.register(Answers)
admin.site.register(AnswerPicture)

