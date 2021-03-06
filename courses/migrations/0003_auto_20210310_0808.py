# Generated by Django 3.0.4 on 2021-03-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_attemptedquestion_choice_question_quizprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, help_text='Explanation to be shown after the question has been answered.', max_length=2000, verbose_name='Explanation'),
        ),
        migrations.AddField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Figure'),
        ),
    ]
