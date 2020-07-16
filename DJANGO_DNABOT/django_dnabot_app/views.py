from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import InputSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Input

# Create your views here.


class InputView(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer

    def create(self, request, *args, **kwargs):
        input_data = request.data
        new_input = Input.objects.create(
            ethanol_stage2=input_data["ethanol_stage2"],
            deep_well_stage4=input_data["deep_well_stage4"],
            construct_csv=input_data["construct_csv"],
            parts_linkers_csv=input_data["parts_linkers_csv"])

        new_input.save()

        serializer = InputSerializer(new_input)
        return Response(serializer.data)
        