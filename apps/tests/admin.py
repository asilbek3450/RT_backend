from django.contrib import admin
from .models import AnswerPicture, Answer, TestPicture, Classes, Themes, TestType, Test
# Register your models here.

admin.site.register(AnswerPicture)
admin.site.register(Answer)
admin.site.register(TestPicture)
admin.site.register(Classes)
admin.site.register(Themes)
admin.site.register(TestType)
admin.site.register(Test)
