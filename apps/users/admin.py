from django.contrib import admin
from .models import HumanType, LanguageChoices, User
# Register your models here.

admin.site.register(HumanType)
admin.site.register(LanguageChoices)
admin.site.register(User)

