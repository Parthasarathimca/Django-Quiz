from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import QuizView,QuizRUDView,QuizAPIView



urlpatterns = [
    
    url(r'^$',QuizView.as_view(),name="qustions"),
    
    url(r'^(?P<pk>\d+)/$',QuizRUDView.as_view(),name="quiz-update-delete"),    
    url(r'^questions/$',QuizAPIView.as_view(),name="quiz-update-delete"), 
]
