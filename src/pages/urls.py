from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),
    path('fixtures', views.fixtures , name = 'fixtures'),
    path('premierLeague', views.premierLeague , name = 'pl'),
    path('quiz', views.quiz , name = 'quiz'),
    path('quizq', views.quizq , name = 'quizquestions'),
    path('quizend', views.quizend , name = 'quizend'),
]