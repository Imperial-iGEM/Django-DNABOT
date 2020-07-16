from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import InputSerializer

from .models import Input

# Create your views here.


class InputView(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer
