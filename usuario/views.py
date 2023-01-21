from django.shortcuts import render, redirect
from . models import Usuario
from .forms import UsuarioForm


def index(request):

    usuario = Usuario.objects.all()
    templateName="index.html"
    context = {
        'u': usuario
    }
    return render(request, templateName, context)


def create(request):
    if request.method == "GET":
        form = UsuarioForm()
        context = {
            'form': form
        }
        return render(request, 'usuario/create.html', context)

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('usuario')


def edit(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == "GET":
        form = UsuarioForm(instance=usuario)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'usuario/edit.html', context)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'usuario/edit.html', context)
