from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import InputSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from .dna_bot.dnabot_app import dnabot

from .models import Input

import os

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
        print(new_input)
        serializer = InputSerializer(new_input)
        print(serializer.data['construct_csv'])
        print(serializer.data['parts_linkers_csv'])

        half_file_path_of_construct = serializer.data['construct_csv']
        half_file_path_of_parts = serializer.data['parts_linkers_csv']
        ethanol2 = serializer.data['ethanol_stage2']
        deep4 = serializer.data['deep_well_stage4']

        full_construct_path = os.path.abspath(half_file_path_of_construct)
        full_parts_path = os.path.abspath(half_file_path_of_parts)

        full_parts_paths = []
        full_parts_paths.append(full_parts_path)

        dnabot(ethanol2,deep4,full_construct_path,full_parts_paths)

        /Users/Benedict/Documents/iGEM/The_Django_Dnabot/Django-DNABOT/DJANGO_DNABOT/DJANGO_DNABOT/template_ot2_scripts
        return Response(serializer.data)
