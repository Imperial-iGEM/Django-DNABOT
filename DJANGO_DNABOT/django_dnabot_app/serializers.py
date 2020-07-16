from django_dnabot_app.models import Input
from rest_framework import serializers


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ['id',
                  'ethanol_stage2',
                  'deep_well_stage4',
                  'construct_csv',
                  'parts_linkers_csv',
                  'python_output_1',
                  'python_output_2',
                  'python_output_3',
                  'python_output_4',
                  ]
