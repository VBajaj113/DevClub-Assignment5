# Generated by Django 4.0.6 on 2022-07-29 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_programme_programme_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_code',
            field=models.CharField(default='', max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='instructorprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='programme',
            name='programme_code',
            field=models.CharField(default='', max_length=5, null=True, unique=True),
        ),
    ]