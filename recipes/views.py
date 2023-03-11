from django.shortcuts import render


# Create your views here.


def home(request):

    return render(request, 'recipesTemp/home.html', context={
        'name': 'Gabriel'
    })


def sobre(request):

    return HttpResponse('sobre')


def contato(request):

    return HttpResponse('contato')
