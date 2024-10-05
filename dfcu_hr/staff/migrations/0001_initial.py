# Generated by Django 4.2.16 on 2024-10-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('id_photo', models.TextField(blank=True, null=True)),
                ('unique_code', models.CharField(max_length=10, unique=True)),
                ('employee_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
