from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Subject, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'title': 'Ex. Class 11 or Informatics Class',
            'description': 'Put a short description of the class',      
            'image': 'You can upload a class photo or leave it blank'
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        #fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        fields = ['creator','slug', 'title', 'klasa', 'description', 'thumbnail']
        help_texts = {
            'title': 'For example. Mathematics, Geography etc.',
            'description':'Provide a brief description of the subject',
            'klasa':'Choose the class for which you will create the subject',
            'thumbnail':'You can put a photo of the subject or it can be left blank'
        }
        labels = {
            'title':'title and subject'
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class TeacherForm(forms.ModelForm): #MesimiForm = TeacherForm
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'subject', 'video_id', 'position', ]
        help_texts = {
            'title':'Enter the title of the lesson',
            'subject':'Choose the subject for which this lesson belongs',
            'video_id':'Enter the Youtube video ID you will upload (<a href="/media/youtube_help.png"> where can i find the ID </a>)',
            'position':'Enter the position number or learning order'
        }
        widgets = {
            'slug': forms.HiddenInput()
        }