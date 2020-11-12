from rest_framework import serializers

from .models import Quiz

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

        
