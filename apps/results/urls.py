from django.urls import path, include

from .views import ResultListCreateView, ResultRetrieveUpdateDestroyView

urlpatterns = [
    path('', ResultListCreateView.as_view()),
    path('<int:pk>', ResultRetrieveUpdateDestroyView.as_view()),
]
