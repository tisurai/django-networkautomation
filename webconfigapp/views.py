import json
import os
from netmiko import ConnectHandler
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from webconfigapp.forms import ShowCommandForm
from webconfigapp.netconnect import nodeconnect

def home(request):
    form = ShowCommandForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Call the netconnect script
            show_cmd = request.POST.get('send_command')
            router_object = nodeconnect(show_cmd)
            output = router_object.get_connect()
            messages.success(request, 'Command sent successfully!')
            
            context = {
                'form': form,
                'data': json.dumps(output)
            }

            return render(request, 'index.html', context)
            
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)