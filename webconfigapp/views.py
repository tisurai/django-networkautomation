from django.shortcuts import render
from webconfigapp.forms import ShowCommandForm


def home(request):
    form = ShowCommandForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)