from django.urls import path, include

from .views import BookTestListCreateView, UserTestListCreateView, OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('', OrderListCreateView.as_view()),
    path('<int:pk>', OrderRetrieveUpdateDestroyView.as_view()),
    path('book_test/', BookTestListCreateView.as_view()),
    path('user_test/', UserTestListCreateView.as_view()),
]
