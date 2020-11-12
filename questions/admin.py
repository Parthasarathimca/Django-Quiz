from django.contrib import admin
from .models import Quiz,QuestionType,marks

admin.site.register(QuestionType)
admin.site.register(Quiz)
admin.site.register(marks)

