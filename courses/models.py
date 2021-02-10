from django.db import models
#from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse


class Klasa(models.Model):  # Klasa=Class
    title = models.CharField(max_length=150)  # title = title
    description = models.TextField(
        max_length=200, null=True)  # description=description
    image = models.ImageField(
        upload_to='cat_images', default='cat_images/default.jpg')  # imazhi=image

    def __str__(self):
        return '{}'.format(self.title)


class Subject(models.Model):  # Lendet=subject
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE)  # krijues = creator
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    klasa = models.ForeignKey(Klasa, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)  # description
    created_at = models.DateTimeField(auto_now=True)  # created_at
    thumbnail = models.ImageField(
        upload_to='course_images', default='default.jpg')  # imazhi_lendes=thumbnail

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    #def get_courses_related_to_memberships(self):
        #return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')  # order_by(pozicioni=position)


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=30)  # title
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # lenda = subject
    video_id = models.CharField(max_length=11)
    position = models.IntegerField()  # pozicioni=position

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.subject.slug, 'lesson_slug': self.slug})
