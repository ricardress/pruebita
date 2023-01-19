from django.shortcuts import render
from . models import Usuario


def index(request):

    usuario = Usuario.objects.all()
    templateName="index.html"
    context = {
        'u': usuario
    }
    return render(request, templateName, context)
