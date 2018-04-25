from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from .models import Quiniela, MemberFixture, GameResult
from .forms import QuinielaForm, GameResultForm


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
    quiniela_games = quiniela.tournament.fixture.all().order_by('match_date')
    initial_data = []
    game_forms = []
    results_formset = modelformset_factory(GameResult, form=GameResultForm, extra=0)
    # Check if user already have a prediction
    prediction = MemberFixture.objects.filter(
        user=request.user.profile,
        tournament=quiniela.tournament
    )
    if request.method == 'POST':
        results_formset = results_formset(request.POST or None)
        if results_formset.is_valid():
            for form in results_formset:
                if form.is_valid():
                    form.save()
    else:
        # Create one in case the user is new to the quiniela
        if not prediction:
            prediction = MemberFixture(
                user=request.user.profile,
                tournament=quiniela.tournament,
            )
            prediction.save()

        prediction = prediction[0]

        for game in quiniela_games:
            aux = prediction.results.filter(game=game)
            if not aux:
                gr = GameResult(
                    game=game,
                    user=request.user.profile,
                )
                gr.save()
                prediction.results.add(gr)

        results_formset = results_formset(queryset=prediction.results.all().order_by('game__match_date'))

    count = 0
    for form in results_formset:
        game_forms.append((quiniela_games[count], form))
        count += 1

    return render(
        request,
        'quiniela_detail.html',
        context={
            'quiniela': quiniela,
            'games': quiniela_games,
            'predictions': game_forms,
            'formset': results_formset
        }
    )