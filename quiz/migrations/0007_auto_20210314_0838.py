# Generated by Django 3.0.4 on 2021-03-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210310_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Figure'),
        ),
    ]