from django.urls import path
from django.contrib.auth.decorators import login_required
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import r

from quiz.views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake


from users.views import Profile, kerkesa

from courses.views import HomeView, AboutView,ErrorView, ContactView, CourseListView, CourseDetailView, LessonDetailView, SearchView, create_class, create_subject, create_lesson

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('error/', ErrorView.as_view(), name='error'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()),
         name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/',
         login_required(LessonDetailView.as_view()), name='lesson_detail'),
    #path('search/', SearchView, name='search_course'),
    path('search/', SearchView, name='search_course'),
    path('create/klasa', create_class, name='create_class'),  # Create / class
    path('create/subject', create_subject, name='create_subject'),  # Create / subject
    path('create/lesson', create_lesson, name='create_lesson'),
    path('profile/', Profile, name='profile'),
    path('kerkesa/', kerkesa, name='kerkesa'),

    url(r'^category/$',
        view=CategoriesListView.as_view(),
        name='category'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='progress'),

    url(r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),
    
    
    
    
      # Create / lesson
]
