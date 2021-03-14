# Generated by Django 3.0.4 on 2021-03-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210125_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.PositiveIntegerField(blank=True, help_text='Number of questions to be answered on each attempt.', null=True, verbose_name='Max Questions'),
        ),
    ]
