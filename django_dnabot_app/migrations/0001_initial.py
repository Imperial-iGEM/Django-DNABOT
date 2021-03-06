# Generated by Django 3.0.8 on 2020-07-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ethanol_stage2', models.CharField(max_length=100)),
                ('deep_well_stage4', models.CharField(max_length=100)),
                ('construct_csv', models.FileField(upload_to='./files/input/constructs')),
                ('parts_linkers_csv', models.FileField(upload_to='./files/input/parts_linkes')),
                ('python_output_1', models.FileField(upload_to='')),
                ('python_output_2', models.FileField(upload_to='')),
                ('python_output_3', models.FileField(upload_to='')),
                ('python_output_4', models.FileField(upload_to='')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
