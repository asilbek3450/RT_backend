from django.urls import path, include

from .views import BookTestViewSet, UserTestListCreateView, OrderListCreateView, OrderRetrieveUpdateDestroyView, \
    BookTestRetrieveUpdateDestroyView

urlpatterns = [
    path('', OrderListCreateView.as_view()),
    path('<int:pk>', OrderRetrieveUpdateDestroyView.as_view()),
    path('book_test/', BookTestViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('book_test/<int:pk>', BookTestRetrieveUpdateDestroyView.as_view()),
    path('user_test/<int:pk>', UserTestListCreateView.as_view()),
]
