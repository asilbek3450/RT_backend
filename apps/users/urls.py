from django.urls import path, include

from .views import UserListCreateView, HumanTypeListCreateView, LanguageChoiceListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('human_type/', HumanTypeListCreateView.as_view()),
    path('language/', LanguageChoiceListCreateView.as_view()),
]
