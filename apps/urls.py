from django.urls import path, include
# Apps urls

urlpatterns = [
    path('user/', include('users.urls', 'user')),
]
