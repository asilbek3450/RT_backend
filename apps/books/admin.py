from django.contrib import admin

from books.models import Book, BookType, Science

# Register your models here.
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Science)
