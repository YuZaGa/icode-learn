import random
from decimal import Decimal
from django.db import models
#from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

class Klasa(models.Model):  # Klasa=Class
    title = models.CharField(max_length=150)  # title = title
    description = models.TextField(
        max_length=200, null=True)  # description=description
    image = models.ImageField(
        upload_to='uploads/', default='cat_images/default.jpg')  # imazhi=image

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
        upload_to='uploads/', default='default.jpg')  # imazhi_lendes=thumbnail

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



#----------------------Adaptive------------------------
class Question(TimeStampedModel):
    ALLOWED_NUMBER_OF_CORRECT_CHOICES = 1

    html = models.TextField(_('Question Text'))
    figure = models.ImageField(upload_to='uploads/',
                               blank=True,
                               null=True,
                               verbose_name=_("Figure"))

    explanation = models.TextField(max_length=2000,
                                   blank=True,
                                   verbose_name=_('Explanation'))

    difficulty = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_("Difficulty"),
        help_text=_("Diffficulty level for the questions"))

    is_published = models.BooleanField(_('Has been published?'), default=False, null=False)
    maximum_marks = models.DecimalField(_('Maximum Marks'), default=4, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.html


class Choice(TimeStampedModel):
    MAX_CHOICES_COUNT = 4

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    is_correct = models.BooleanField(_('Is this answer correct?'), default=False, null=False)
    html = models.TextField(_('Choice Text'))

    def __str__(self):
        return self.html


class QuizProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(_('Total Score'), default=0, decimal_places=2, max_digits=10)
    tip = 0
    ip= models.DecimalField(_('Individual Proficiency'), default=1, decimal_places=2, max_digits=10)
    #
    # progresss = models.DecimalField(_('progress'), default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'<QuizProfile: user={self.user}>'

    def get_new_question(self):
        used_questions_pk = Question.objects.filter(difficulty__gt=self.ip)
        remaining_questions = Question.objects.exclude(pk__in=used_questions_pk) 
        if not remaining_questions.exists():
            return 
        return random.choice(remaining_questions)

    def create_attempt(self, question):
        attempted_question = AttemptedQuestion(question=question, quiz_profile=self)
        attempted_question.save()

    def evaluate_attempt(self, attempted_question, selected_choice):
        if attempted_question.question_id != selected_choice.question_id:
            return

        attempted_question.selected_choice = selected_choice
        if selected_choice.is_correct is True:
            attempted_question.is_correct = True
            attempted_question.marks_obtained = attempted_question.question.maximum_marks

        attempted_question.save()
        self.update_score()
        self.progress()



    def evaluate_ip(self, attempted_question, selected_choice):
        diff = attempted_question.question.difficulty
        if attempted_question.question_id != selected_choice.question_id:
            tip = (10-diff)/10
            self.ip = self.ip - Decimal(tip)
            if self.ip < 1:
                self.ip = 1

        attempted_question.selected_choice = selected_choice
        if selected_choice.is_correct is True:
            attempted_question.is_correct = True
            attempted_question.marks_obtained = attempted_question.question.maximum_marks
            tip = diff/10
            self.ip = self.ip + Decimal(tip)
        else:
            tip = (10-diff)/10
            self.ip = self.ip - Decimal(tip)
            if self.ip < 1:
                self.ip = 1

        attempted_question.save()
        self.save()
        return self.ip

    def progress(self):
        used_questions_pk = AttemptedQuestion.objects.filter(quiz_profile=self).values_list('question__pk', flat=True)
        remaining_questions = Question.objects.exclude(pk__in=used_questions_pk)
        try :
            progresss=used_questions_pk.count()/(used_questions_pk.count()+remaining_questions.count())*100
        except:
            progresss = 0
        self.save()
        return progresss
 

    def update_score(self):
        marks_sum = self.attempts.filter(is_correct=True).aggregate(
            models.Sum('marks_obtained'))['marks_obtained__sum']
        self.total_score = marks_sum or 0
        self.save()


class AttemptedQuestion(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_profile = models.ForeignKey(QuizProfile, on_delete=models.CASCADE, related_name='attempts')
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(_('Was this attempt correct?'), default=False, null=False)
    marks_obtained = models.DecimalField(_('Marks Obtained'), default=0, decimal_places=2, max_digits=6)

    def get_absolute_url(self):
        return f'/submission-result/{self.pk}/'

