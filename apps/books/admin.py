from django.contrib import admin
from books.models.book import Book, BookType
from books.models.science import Science

# Register your models here.
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Science)
