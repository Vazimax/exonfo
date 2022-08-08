from dataclasses import field
from django.shortcuts import render
from .models import MathWord, PCWord, SVTWord

def home(request):

    return render(request,'home.html')

def pc(request):
    
    return render(request,'pc/pc.html')

def pc_general(request):

    general_words = PCWord.objects.all().filter(field='Generals')
    context = {
        'general_words':general_words
    }

    return render(request,'pc/pc_general.html',context)

def pc_mechanics(request):

    mechanic_words = PCWord.objects.all().filter(field='Mechanics')
    context = {
        'mechanic_words':mechanic_words
    }

    return render(request,'pc/mechanics.html',context)

def pc_electricity(request):

    electricity_words = PCWord.objects.all().filter(field='Electricity')
    context = {
        'electricity_words':electricity_words
    }

    return render(request,'pc/electricity.html',context)

def pc_optics(request):

    optics_words = PCWord.objects.all().filter(field='Optics')
    context = {
        'optics_words':optics_words
    }

    return render(request,'pc/optics.html',context)

def pc_waves(request):

    waves_words = PCWord.objects.all().filter(field='Waves')
    context = {
        'waves_words':waves_words
    }

    return render(request,'pc/waves.html',context)

def pc_nuclear(request):

    nuclear_words = PCWord.objects.all().filter(field='Nuclear transformation')
    context = {
        'nuclear_words':nuclear_words
    }

    return render(request,'pc/nuclear.html',context)

def pc_matter(request):

    matter_words = PCWord.objects.all().filter(field='Matter')
    context = {
        'matter_words':matter_words
    }

    return render(request,'pc/matter.html',context)