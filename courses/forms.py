from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Subject, Lesson

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['html', 'is_published','figure','explanation','difficulty']
        widgets = {
            'html': forms.Textarea(attrs={'rows': 3, 'cols': 80}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['html', 'is_correct']
        widgets = {
            'html': forms.Textarea(attrs={'rows': 2, 'cols': 80}),
        }


class ChoiceInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ChoiceInlineFormset, self).clean()

        correct_choices_count = 0
        for form in self.forms:
            if not form.is_valid():
                return

            if form.cleaned_data and form.cleaned_data.get('is_correct') is True:
                correct_choices_count += 1

        try:
            assert correct_choices_count == Question.ALLOWED_NUMBER_OF_CORRECT_CHOICES
        except AssertionError:
            raise forms.ValidationError(_('Exactly one correct choice is allowed.'))


User = get_user_model()





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