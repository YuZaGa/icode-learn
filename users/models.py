from django.db import models
import os
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(
        default='default.png', upload_to='uploads/')
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        # return self.user.username + ' Profile'
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        print(os.getcwd())
        os.listdir()  # to check the location for FileNotFound Error
        # please check the path where pics are stores, here it is giving an error
        img = Image.open(self.profile_pic.path)
        if img.height > 100 or img.width > 100:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class Kerkesat(models.Model):  # class Requests
    profili = models.ForeignKey(Profile, on_delete=models.CASCADE)  # profile
    emri = models.CharField(max_length=50)  # name
    email = models.EmailField(max_length=254)
    numri_tel = models.CharField(max_length=15)  # mobile_number

    def __str__(self):
        return self.profili.user.username
