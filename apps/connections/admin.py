from django.contrib import admin
from connections.models.book_test import BookTest
from connections.models.orders import Order
from connections.models.user_test import UserTest
# Register your models here.

admin.site.register(BookTest)
admin.site.register(Order)
admin.site.register(UserTest)

