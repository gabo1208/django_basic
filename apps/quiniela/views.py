import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory, formset_factory

from .models import Quiniela, MemberFixture, GameResult, Group, MemberFixture
from .forms import QuinielaForm, GameResultForm, BlockedGameResultForm, InviteUsersForm
from apps.users.models import Profile


# User quiniela's view
@login_required
def quiniela_index(request):
    if request.method == 'POST':
        form = QuinielaForm(request.POST)
        if form.is_valid():
            quiniela = form.save(commit=False)
            quiniela.admin = request.user.profile
            quiniela.save()
            quiniela.members.add(request.user.profile)
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

# View to process all quiniela details
@login_required
def quiniela_details(request, quiniela_id):
    quiniela = get_object_or_404(Quiniela, id=quiniela_id)
    quiniela_games = quiniela.tournament.fixture.all().order_by('match_datetime')
    group_prefixes = ['group1']
    initial_data = []
    groups_formsets = []
    formsets = []
    invite_formset = formset_factory(InviteUsersForm)
    results_formset = modelformset_factory(GameResult, form=GameResultForm, extra=0)
    blocked_results_formset = modelformset_factory(GameResult, form=BlockedGameResultForm, extra=0)
    
    # Update current predictions from user
    if request.method == 'POST':
        invite_formset = invite_formset(request.POST or None, prefix='invite_users')
        if invite_formset.is_valid():
            for form in invite_formset:
                if form.is_valid():
                    if form.cleaned_data.get('users'):
                        for user in form.cleaned_data.get('users').replace(' ','').split(';'):
                            user = Profile.objects.filter(user__username=user) or Profile.objects.filter(user__email=user)
                            if user and user[0] not in quiniela.members.all():
                                quiniela.members.add(user[0])
        else:
            print(invite_formset.errors)

        for prefix in group_prefixes:
            formsets.append(results_formset(request.POST or None, prefix=prefix))

        count = 0
        for game in quiniela_games:
            if quiniela_games[count].match_datetime <= timezone.now() - datetime.timedelta(hours=4):
                count += 1

        for formset in formsets:
            if formset.is_valid():
                for form in formset:
                    if form.is_valid():
                        if quiniela_games[count].match_datetime > timezone.now() - datetime.timedelta(hours=4):
                            form.save()
                    else:
                        print(form.errors)
                            
                    count += 1
            else:
                print(formset.errors)

        formsets = []
    else:
        invite_formset = invite_formset(prefix='invite_users')

    # Check if user already have a prediction
    prediction = MemberFixture.objects.filter(
        user=request.user.profile,
        tournament=quiniela.tournament
    )

    # Create predictions for each game in case the user is new to the quiniela
    # or the game is recently added to that quiniela
    if not prediction:
        prediction = MemberFixture(
            user=request.user.profile,
            tournament=quiniela.tournament,
        )
        prediction.save()
    else:
        prediction = prediction[0]

    qset = prediction.results.all().order_by('game__match_datetime')

    init = 0
    end = 15
    for game in quiniela_games:
        aux = qset.filter(game=game)
        if game.match_datetime <= timezone.now() - datetime.timedelta(hours=4):
            init += 1

            if init >= end:
                init = end + 1
                end += 16

        if not aux:
            gr = GameResult(
                game=game,
                user=request.user.profile,
            )
            gr.save()
            prediction.results.add(gr)

    # Populate the passed Games GameResultForms with BlockedGameResultForms
    if init > 0:
        formsets.append(blocked_results_formset(queryset=qset[0:init]))

    # Create and populate new formsets with the prediction data
    lim = init//16
    for prefix in group_prefixes[lim:]:
        formsets.append(results_formset(queryset=qset[init:end+1], prefix=prefix))
        init = end + 1
        end += 16

    # Poputa template context vars
    count = 0
    for formset in formsets:
        if count % 16 == 0:
            group_forms = []

        for form in formset:
            group_forms.append((quiniela_games[count], form))
            count += 1

        if count % 16 == 0:
            groups_formsets.append((group_forms, formset.management_form))

    if count % 16 != 0:
        groups_formsets.append((group_forms, formset.management_form))

    leaders = MemberFixture.objects.filter(tournament=quiniela.tournament).order_by('score')
    pendings = []

    for user in quiniela.members.all():
        if not leaders.filter(user=user):
            pendings.append(user)

    return render(
        request,
        'quiniela_detail.html',
        context={
            'quiniela': quiniela,
            'group_predictions': groups_formsets,
            'leaders': MemberFixture.objects.filter(tournament=quiniela.tournament).order_by('score'),
            'pendings': pendings,
            'groups': Group.objects.filter(tournament=quiniela.tournament).order_by('name'),
            'invite_formset': invite_formset
        }
    )

# View to delete a quiniela
@login_required
def quiniela_delete(request, quiniela_id):
    quiniela = get_object_or_404(Quiniela, id=quiniela_id)
    quiniela.delete()
    return redirect('quiniela:user_quinielas')