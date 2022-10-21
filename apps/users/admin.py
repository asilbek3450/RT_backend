from django.contrib import admin

from users.model import LanguageChoices, HumanType, User

admin.site.register(User)
admin.site.register(HumanType)
admin.site.register(LanguageChoices)
