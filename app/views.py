from dataclasses import field
from django.shortcuts import render
from .models import MathWord, PCWord, SVTWord
from .filters import OrderFilter


def home(request):

    return render(request,'home.html')

# Physics & Chemistry :

def pc(request):
    
    return render(request,'pc/pc.html')

def pc_general(request):

    general_words = PCWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'general_words':general_words,
        'filter':filter,
    }

    return render(request,'pc/pc_general.html',context)

def pc_mechanics(request):

    general_words = PCWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'general_words':general_words,
        'filter':filter,
    }

    return render(request,'pc/pc_general.html',context)

def pc_electricity(request):

    electricity_words = PCWord.objects.all().filter(field='Electricity')
    filter = OrderFilter(request.GET,queryset=electricity_words)
    electricity_words = filter.qs
    context = {
        'electricity_words':electricity_words,
        'filter':filter,
    }

    return render(request,'pc/electricity.html',context)

def pc_optics(request):

    optics_words = PCWord.objects.all().filter(field='Optics')
    filter = OrderFilter(request.GET,queryset=optics_words)
    optics_words = filter.qs
    context = {
        'optics_words':optics_words,
        'filter':filter,
    }

    return render(request,'pc/optics.html',context)

def pc_waves(request):

    waves_words = PCWord.objects.all().filter(field='Waves')
    filter = OrderFilter(request.GET,queryset=waves_words)
    waves_words = filter.qs
    context = {
        'waves_words':waves_words,
        'filter':filter,
    }

    return render(request,'pc/waves.html',context)

def pc_nuclear(request):

    nuclear_words = PCWord.objects.all().filter(field='Nuclear transformation')
    filter = OrderFilter(request.GET,queryset=nuclear_words)
    nuclear_words = filter.qs
    context = {
        'nuclear_words':nuclear_words,
        'filter':filter,
    }

    return render(request,'pc/nuclear.html',context)

def pc_matter(request):

    matter_words = PCWord.objects.all().filter(field='Matter')
    filter = OrderFilter(request.GET,queryset=matter_words)
    matter_words = filter.qs
    context = {
        'matter_words':matter_words,
        'filter':filter,
    }

    return render(request,'pc/matter.html',context)

def pc_measurement(request):

    measurement_words = PCWord.objects.all().filter(field='Measurements in chemistry')
    filter = OrderFilter(request.GET,queryset=measurement_words)
    measurement_words = filter.qs
    context = {
        'measurement_words':measurement_words,
        'filter':filter,
    }

    return render(request,'pc/measurement.html',context)

def pc_reactions(request):

    reactions_words = PCWord.objects.all().filter(field='Chemical reactions')
    filter = OrderFilter(request.GET,queryset=reactions_words)
    reactions_words = filter.qs
    context = {
        'reactions_words':reactions_words,
        'filter':filter,
    }

    return render(request,'pc/reactions.html',context)

def pc_organic(request):

    organic_words = PCWord.objects.all().filter(field='Organic chemistry')
    filter = OrderFilter(request.GET,queryset=organic_words)
    organic_words = filter.qs
    context = {
        'organic_words':organic_words,
        'filter':filter,
    }

    return render(request,'pc/organic.html',context)
    
# SVT :

def svt(request):
    
    return render(request,'svt/svt.html')

def svt_general(request):

    general_words = SVTWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'svt_general_words':general_words,
        'filter':filter,
    }

    return render(request,'svt/svt_general.html',context)


def svt_ecology(request):

    ecology_words = SVTWord.objects.all().filter(field='Ecology')
    filter = OrderFilter(request.GET,queryset=ecology_words)
    ecology_words = filter.qs
    context = {
        'svt_ecology_words':ecology_words,
        'filter':filter,
    }

    return render(request,'svt/svt_ecology.html',context)

def svt_rep_plant(request):

    rep_plant_words = SVTWord.objects.all().filter(field='Reproduction in plants')
    filter = OrderFilter(request.GET,queryset=rep_plant_words)
    rep_plant_words = filter.qs
    context = {
        'svt_rep_plant_words':rep_plant_words,
        'filter':filter,
    }

    return render(request,'svt/svt_rep_plant.html',context)

def svt_geology(request):

    geology_words = SVTWord.objects.all().filter(field='Geology')
    filter = OrderFilter(request.GET,queryset=geology_words)
    geology_words = filter.qs
    context = {
        'svt_geology_words':geology_words,
        'filter':filter,
    }

    return render(request,'svt/svt_geology.html',context)

def svt_genetics(request):

    genetic_words = SVTWord.objects.all().filter(field='Genetics')
    filter = OrderFilter(request.GET,queryset=genetic_words)
    genetic_words = filter.qs
    context = {
        'svt_genetic_words':genetic_words,
        'filter':filter,
    }

    return render(request,'svt/svt_genetics.html',context)

def svt_organic(request):

    organic_words = SVTWord.objects.all().filter(field='Organic matter')
    filter = OrderFilter(request.GET,queryset=organic_words)
    organic_words = filter.qs
    context = {
        'svt_organic_words':organic_words,
        'filter':filter,
    }

    return render(request,'svt/svt_organic.html',context)

def svt_nerves(request):

    nerves_words = SVTWord.objects.all().filter(field='Nerves: Neurons and hormones')
    filter = OrderFilter(request.GET,queryset=nerves_words)
    nerves_words = filter.qs
    context = {
        'svt_nerves_words':nerves_words,
        'filter':filter,
    }

    return render(request,'svt/svt_nerves.html',context)

def svt_rep_human(request):

    rep_human_words = SVTWord.objects.all().filter(field='Reproduction in humans ')
    filter = OrderFilter(request.GET,queryset=rep_human_words)
    rep_human_words = filter.qs
    context = {
        'svt_rep_human_words':rep_human_words,
        'filter':filter,
    }

    return render(request,'svt/svt_rep_human.html',context)

def svt_immunity(request):

    immunity_words = SVTWord.objects.all().filter(field='Immunology')
    filter = OrderFilter(request.GET,queryset=immunity_words)
    immunity_words = filter.qs
    context = {
        'svt_immunity_words':immunity_words,
        'filter':filter,
    }

    return render(request,'svt/svt_immunity.html',context)

# MATH :

def math(request):
    
    return render(request,'math/math.html')

def math_general(request):

    general_words = MathWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'math_general_words':general_words,
        'filter':filter,
    }

    return render(request,'math/math_general.html',context)

def math_alca(request):

    alca_words = MathWord.objects.all().filter(field='Algebra and Calculus')
    filter = OrderFilter(request.GET,queryset=alca_words)
    alca_words = filter.qs
    context = {
        'math_alca_words':alca_words,
        'filter':filter,
    }

    return render(request,'math/alca.html',context)

def math_geometry(request):

    geometry_words = MathWord.objects.all().filter(field='Geometry')
    filter = OrderFilter(request.GET,queryset=geometry_words)
    geometry_words = filter.qs
    context = {
        'geometry_words':geometry_words,
        'filter':filter,
    }

    return render(request,'math/geometry.html',context)