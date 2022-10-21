from django.contrib import admin

from .models.book import Book, BookType
from .models.science import Science

# Register your models here.
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Science)
