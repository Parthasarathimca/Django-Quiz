from django.db import models
from django.contrib.auth.models import User

class QuestionType(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table="quesion_type"

class Quiz(models.Model):
    question_type=models.ForeignKey(QuestionType,on_delete = models.CASCADE)
    quistion = models.CharField(max_length=100)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3= models.CharField(max_length=100)
    option4= models.CharField(max_length=100)
    answer= models.CharField(max_length=100)

    class Meta:
        db_table="quiz"

class marks(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete = models.CASCADE)
    marks=  models.IntegerField(default=0)
    
    class Meta:
        db_table="marks"



