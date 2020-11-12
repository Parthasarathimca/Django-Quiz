from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import QuizSerializer
from .models import Quiz
from rest_framework import viewsets,generics


class QuizView(APIView):
    
    def get(self, request):
        data={}
        template="index.html"
        quiz_queryset =Quiz.objects.all()
        data['quiz']=quiz_queryset
        return render(request,template,data)
        
class QuizRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_filed='pk'
    serializer_class=QuizSerializer
    def get_queryset(self):
        return Quiz.objects.all()   


""" for list view to show all questions """
class QuizAPIView(generics.ListAPIView):
    lookup_filed='pk'
    serializer_class=QuizSerializer
    def get_queryset(self):
        return Quiz.objects.all()   

    