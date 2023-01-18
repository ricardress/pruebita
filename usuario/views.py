from django.shortcuts import render


def index(request):

    templateName="index.html"
    return render(request, templateName)
