from django.urls import path, include

urlpatterns = [
    path('book/', include('books.urls')),
    path('user/', include('users.urls')),
    path('test/', include('tests.urls')),
#     path('connection/', include('connections.urls')),
#     path('result/', include('results.urls')),
#
]
