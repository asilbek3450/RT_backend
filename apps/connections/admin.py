from django.contrib import admin
from .models.orders import Order
from .models.book_test import BookTest
from .models.user_test import UserTest

# Register your models here.
admin.site.register(BookTest)
admin.site.register(Order)
admin.site.register(UserTest)

