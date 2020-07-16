from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from django_dnabot_app.serializers import InputSerializer

from django_dnabot_app.models import Input

# Create your views here.

class InputList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = InputSerializer

class InputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = InputSerializer