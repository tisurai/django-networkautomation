import os
from netmiko import ConnectHandler
from django.shortcuts import render
from django.http import JsonResponse
from webconfigapp.forms import ShowCommandForm
from webconfigapp.netconnect import nodeconnect


def home(request):
    form = ShowCommandForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Call the netconnect
            show_cmd = request.POST.get('send_command')
            router_object = nodeconnect(show_cmd)
            return JsonResponse({'data':router_object})
            
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)