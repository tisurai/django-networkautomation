import json
import os
from netmiko import ConnectHandler
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from webconfigapp.forms import ShowCommandForm
from webconfigapp.netconnect import nodeconnect
from jinja2 import (
    Environment, 
    FileSystemLoader, 
    PackageLoader, 
    select_autoescape
)

def home(request):
    form = ShowCommandForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Call the netconnect
            show_cmd = request.POST.get('send_command')
            router_object = nodeconnect(show_cmd)
            output = router_object.get_connect()

            ENV = Environment(
                loader = PackageLoader('webconfigapp', 'templates/configs'),
                autoescape = select_autoescape(['html', 'j2'])
            )
            template = ENV.get_template('cisco.j2')
            jinja_output = template.render(link=json.dumps(output))
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