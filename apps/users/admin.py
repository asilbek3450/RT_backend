from django.contrib import admin
from users.models import HumanType, LanguageChoices, User
# Register your models here.

admin.site.register(User)
admin.site.register(HumanType)
admin.site.register(LanguageChoices)
