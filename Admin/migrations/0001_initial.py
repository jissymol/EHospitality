# Generated by Django 5.1.3 on 2025-01-23 14:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('location', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='doctor_media')),
                ('date', models.DateField(default=datetime.date.today)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password1', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
            ],
        ),
    ]
