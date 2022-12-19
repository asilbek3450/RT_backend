from django.urls import path, include

from .views import BookViewSet, BookRetrieveUpdateDestroyView, ScienceListCreateView, BookTypeListCreateView

urlpatterns = [
    path('', BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', BookRetrieveUpdateDestroyView.as_view()),
    path('science/', ScienceListCreateView.as_view()),
    path('booktype/', BookTypeListCreateView.as_view()),
]
