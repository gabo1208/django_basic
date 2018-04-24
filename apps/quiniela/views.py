from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Quiniela
from .forms import QuinielaForm


# User quiniela's view
@login_required
def quiniela_index(request):
    if request.method == 'POST':
        form = QuinielaForm(request.POST)
        if form.is_valid():
            quiniela = form.save()
            quiniela.members.add(request.user.profile)
            quiniela.save()
    else:
        form = QuinielaForm()

    return render(
        request,
        'quiniela_index.html',
        context={
            'quinielas':Quiniela.objects.filter(members=request.user.profile),
            'form': form,
        }
    )

@login_required
def quiniela_details(request, quiniela_id):
	quiniela = get_object_or_404(Quiniela, id=quiniela_id)
	return render(request, 'quiniela_detail.html', context={'quiniela': quiniela})