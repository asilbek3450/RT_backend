from django.urls import path, include

from .views import BookListCreateView, BookRetrieveUpdateDestroyView, ScienceListCreateView, BookTypeListCreateView

urlpatterns = [
    path('', BookListCreateView.as_view()),
    path('<int:pk>', BookRetrieveUpdateDestroyView.as_view()),
    path('science/', ScienceListCreateView.as_view()),
    path('booktype/', BookTypeListCreateView.as_view()),
]
