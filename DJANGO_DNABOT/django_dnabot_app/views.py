from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_dnabot_app.serializers import InputSerializer

# Create your views here.

class InputViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = InputSerializer