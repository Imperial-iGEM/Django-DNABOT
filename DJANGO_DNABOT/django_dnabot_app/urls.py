from django.urls import path
from django_dnabot_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Inputs/', views.InputList.as_view()),
    path('Inputs/<int:pk>/', views.InputDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)