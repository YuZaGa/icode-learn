# Generated by Django 3.0.4 on 2021-03-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_quizprofile_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasa',
            name='image',
            field=models.ImageField(default='cat_images/default.jpg', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Figure'),
        ),
        migrations.AlterField(
            model_name='quizprofile',
            name='ip',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Individual Proficiency'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
