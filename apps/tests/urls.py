from django.urls import path, include

from .views import AnswerPictureView, AnswerView, TestPictureView, ClassesView, ThemesView, TestTypeView, TestView, \
    TestRetrieveUpdateDestroyView

urlpatterns = [
    path('', TestView.as_view()),
    path('<int:pk>', TestRetrieveUpdateDestroyView.as_view()),
    path('answer_picture/', AnswerPictureView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('test_picture/', TestPictureView.as_view()),
    path('classes/', ClassesView.as_view()),
    path('themes/', ThemesView.as_view()),
    path('test_type/', TestTypeView.as_view()),
]

