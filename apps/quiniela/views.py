from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# User quiniela's view
@login_required
def quiniela_index(request):
    return render(request, 'index.html', context={'msg': "Hello, world. You're at index."})
