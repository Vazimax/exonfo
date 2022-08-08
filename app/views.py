from dataclasses import field
from django.shortcuts import render
from .models import MathWord, PCWord, SVTWord

def home(request):

    return render(request,'home.html')

def pc(request):
    
    return render(request,'pc.html')

def pc_mechanics(request):

    mechanic_words = PCWord.objects.all().filter(field='Mechanics')
    context = {
        'mechanic_words':mechanic_words
    }

    return render(request,'mechanics.html',context)

def pc_electricity(request):

    electricity_words = PCWord.objects.all().filter(field='Electricity')
    context = {
        'electricity_words':electricity_words
    }

    return render(request,'electricity.html',context)