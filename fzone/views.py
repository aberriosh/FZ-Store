from django.shortcuts import render

def ini(request):
    return render(
        request,
        'inicio.html',
        context={}
    )

def consolas(request):
    return render(
        request,
        'consolas.html',
        context={}
    )

def figuras(request):
    return render(
        request,
        'figuras.html',
        context={}
    )

def videojuegos(request):
    return render(
        request,
        'videojuegos.html',
        context={}
    )

def tcg(request):
    return render(
        request,
        'tcg.html',
        context={}
    )

def retro(request):
    return render(
        request,
        'consolasRetro.html',
        context={}
    )