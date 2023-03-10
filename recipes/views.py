from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request, 'recipesTemp/home.html', context={
        'name': 'Gabriel'
    })


def sobre(request):

    return HttpResponse('sobre')


def contato(request):

    return HttpResponse('contato')
