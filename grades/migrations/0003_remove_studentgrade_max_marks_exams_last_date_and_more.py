# Generated by Django 4.0.6 on 2022-07-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_alter_studentgrade_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgrade',
            name='max_marks',
        ),
        migrations.AddField(
            model_name='exams',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Submission Deadline'),
        ),
        migrations.AddField(
            model_name='exams',
            name='max_marks',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='studentgrade',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('B-', 'B-'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('F', 'F'), ('I', 'I')], default='I', max_length=2),
        ),
    ]