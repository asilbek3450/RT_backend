from django.contrib import admin

from connections.models import BookTest, UserTest, Order

# Register your models here.
admin.site.register(BookTest)
admin.site.register(UserTest)
admin.site.register(Order)
