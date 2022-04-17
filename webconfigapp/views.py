from django.shortcuts import render
from webconfigapp.forms import ShowCommandForm


def home(request):
    form = ShowCommandForm(request.POST or None)

    if request.is_ajax():
        if form.is_valid():
            # Call the netconnect
            show_cmd = request.POST.get('send_command')
            router_object = nodeconnect(show_cmd)
            return JsonResponse({'data':router_object})
            
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)