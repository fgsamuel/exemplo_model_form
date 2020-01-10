from django.shortcuts import render, redirect

# Create your views here.
from exemplo.forms import PessoaForm
from exemplo.models import Pessoa


def index(request):

    if request.method == 'GET':
        pessoas = Pessoa.objects.all()

        form = PessoaForm()

        context = {
            'pessoas': pessoas,
            'form': form,
        }
        return render(request, 'exemplo/index.html', context)
    elif request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pessoas = Pessoa.objects.all()

            context = {
                'pessoas': pessoas,
                'form': form,
            }
            return render(request, 'exemplo/index.html', context)



