import datetime

from django.utils import timezone
from django.http import HttpResponse
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
    is_member = True
    inviting = False
    active = 0
    phases_limit = 16
    quiniela = get_object_or_404(Quiniela, id=quiniela_id)
    quiniela_games = quiniela.tournament.fixture.all().order_by('match_datetime')
    phases_prefixes = ['group1', 'group2', 'group3']
    initial_data = []
    groups_formsets = []
    formsets = []
    invite_errors = []
    invite_notifications = []
    invite_fs = formset_factory(InviteUsersForm)
    results_formset = modelformset_factory(GameResult, form=GameResultForm, extra=0)
    blocked_results_formset = modelformset_factory(GameResult, form=BlockedGameResultForm, extra=0)

    # Matchdays separation for active tab, 1st leg
    if datetime.datetime.now() <= datetime.datetime(2018, 6, 19, 12):
        active += 1
    # 2nd leg
    elif datetime.datetime.now() <= datetime.datetime(2018, 6, 24, 15):
        active += 1
    # 3rd leg
    elif datetime.datetime.now() <= datetime.datetime(2018, 6, 28, 15):
        active += 1
    # 8th 
    elif datetime.datetime.now() <= datetime.datetime(2018, 7, 3, 15):
        active += 1
    # Quarters
    elif datetime.datetime.now() <= datetime.datetime(2018, 7, 7, 15):
        active += 1
    # Semifinals
    elif datetime.datetime.now() <= datetime.datetime(2018, 7, 11, 15):
        active += 1
    # 3rd Place
    elif datetime.datetime.now() <= datetime.datetime(2018, 7, 14, 12):
        active += 1
    # Final
    elif datetime.datetime.now() <= datetime.datetime(2018, 7, 15, 12):
        active += 1
    # To active leaderboards tab
    if request.GET.get('leaderboard') == 'True':
        active = 0

    # To maintain url vars
    if request.GET.get('joined') == 'True':
        invite_notifications.append('You have joined this Quiniela =)!')
        inviting = True

    # If user is member of this Quiniela
    if request.user.profile in quiniela.members.all():
        # Update current predictions from user
        if request.method == 'POST':
            # To Clear url vars
            if request.GET.get('joined') == 'True':
                inviting = False
                invite_notifications = []

            # Check if user has added other users
            invite_formset = invite_fs(request.POST or None, prefix='invite_users')
            if invite_formset.is_valid():
                for form in invite_formset:
                    if form.is_valid():
                        if form.cleaned_data.get('users'):
                            active = 0
                            inviting = True
                            for user in form.cleaned_data.get('users').replace(' ','').split(';'):
                                useraux = Profile.objects.filter(user__username=user) or Profile.objects.filter(user__email=user)
                                if useraux and useraux[0] not in quiniela.members.all():
                                    quiniela.members.add(useraux[0])
                                    invite_notifications.append('User ' + user + ' has been added to this Quiniela!')
                                elif useraux:
                                    invite_errors.append('User ' + user + ' is already in this Quiniela.')
                                else:
                                    invite_errors.append('User ' + user + ' does not exists.')
            else:
                print(invite_formset.errors)

            # Check Games passed by now
            count = 0
            for game in quiniela_games:
                if quiniela_games[count].match_datetime <= timezone.now() - datetime.timedelta(hours=4):
                    count += 1

            for prefix in phases_prefixes:
                formsets.append(results_formset(request.POST or None, prefix=prefix))

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

        # Check if user already have a prediction for this quiniela
        prediction = MemberFixture.objects.filter(
            user=request.user.profile,
            tournament=quiniela.tournament,
            quiniela=quiniela
        )

        # Create predictions for each game in case the user is new to the quiniela
        # or the game is recently added to that quiniela
        if not prediction:
            prediction = MemberFixture(
                user=request.user.profile,
                tournament=quiniela.tournament,
                quiniela=quiniela,
            )
            prediction.save()
        else:
            prediction = prediction[0]

        # MemberFixture from user ordered by date
        qset = prediction.results.order_by('game__match_datetime')
        init = 0
        lim = 0 # To save the last phase
        end = phases_limit
        # Initialize passed games results with blocked gameforms
        for game in quiniela_games:
            aux = qset.filter(game=game)
            if game.match_datetime <= timezone.now() - datetime.timedelta(hours=4):
                init += 1
                # Phase limit border cases
                if init == end:
                    formsets.append(blocked_results_formset(queryset=qset[end-phases_limit:init]))
                    lim += 1
                    (init, end, phases_limit) = phasesLimit(init, end, phases_limit)
                    if init < 0:
                        break

            # If that game prediction does not exist, create it
            if not aux:
                gr = GameResult(
                    game=game,
                    user=request.user.profile,
                )
                gr.save()
                prediction.results.add(gr)

        # If the number of blocked results isn't round with a group number limit
        if init != end and init > 0:
            formsets.append(blocked_results_formset(queryset=qset[end-phases_limit:init]))

        # Create and populate new formsets with the prediction data starting from the last BlockedGameResult
        for prefix in phases_prefixes[lim:]:
            formsets.append(results_formset(queryset=qset[init:end], prefix=prefix))
            (init, end, phases_limit) = phasesLimit(init, end, phases_limit)
            if init < 0:
                break

        # Populate template context vars
        phases_limit = 16
        end = phases_limit
        count = 0
        prefix = 0
        for formset in formsets:
            if count % phases_limit == 0:
                group_forms = []

            for form in formset:
                group_forms.append((quiniela_games[count], form))
                count += 1

            if count % phases_limit == 0:
                groups_formsets.append((group_forms, formset.management_form, phases_prefixes[prefix]))
                prefix += 1
                (init, end, phases_limit) = phasesLimit(count, end, phases_limit)
                if init < 0:
                    break

        if count % phases_limit != 0:
            groups_formsets.append((group_forms, formset.management_form, phases_prefixes[prefix]))

    # If request.user is not in this quinielas members
    else:
        is_member = False
        init = 0
        end = phases_limit
        count = 0
        for game in quiniela_games:
            if count % phases_limit == 0:
                group_forms = []

            group_forms.append((game, None))
            count += 1
            if count % phases_limit == 0:
                groups_formsets.append((group_forms, None, phases_prefixes[prefix]))
                prefix += 1
                (init, end, phases_limit) = phasesLimit(count, end, phases_limit)
                if init < 0:
                    break

        if count % phases_limit != 0:
            groups_formsets.append((group_forms, None, phases_prefixes[count//phases_limit]))

    # Request and request.user independant code and initializations
    invite_formset = invite_fs(prefix='invite_users')
    leaders = MemberFixture.objects.filter(
                tournament=quiniela.tournament,
                quiniela=quiniela
            ).order_by('score')

    pendings = []

    for user in quiniela.members.all():
        if not leaders.filter(user=user):
            pendings.append(user)

    return render(
        request,
        'quiniela_details.html',
        context={
            'is_member': is_member,
            'quiniela': quiniela,
            'active': active,
            'inviting': inviting,
            'group_predictions': groups_formsets,
            'leaders': leaders,
            'pendings': pendings,
            'groups': Group.objects.filter(tournament=quiniela.tournament).order_by('name'),
            'invite_formset': invite_formset,
            'invite_errors': invite_errors,
            'invite_notifications': invite_notifications,
        }
    )


# View to delete a quiniela
@login_required
def quiniela_join(request, quiniela_id):
    quiniela = get_object_or_404(Quiniela, id=quiniela_id)
    quiniela.members.add(request.user.profile)
    response = HttpResponse()
    response = redirect('quiniela:quiniela_details', quiniela_id=quiniela_id)
    response['Location'] += '?leaderboard=True&joined=True'
    return response


# View to delete a quiniela
@login_required
def quiniela_delete(request, quiniela_id):
    quiniela = get_object_or_404(Quiniela, id=quiniela_id)
    quiniela.delete()
    return redirect('quiniela:user_quinielas')


def phasesLimit(init, end, phases_limit):
    if end <= 48:
        init = end
        end += phases_limit
    # 8ths
    elif end <= 56:
        phases_limit //= 2
        init = end
        end += phases_limit
    # 4ths
    elif end <= 60:
        phases_limit //= 2
        init = end
        end += phases_limit
    # Semis
    elif end <= 62:
        phases_limit //= 2
        init = end
        end += phases_limit
    # Third
    elif end <= 63:
        phases_limit //= 2
        init = end
        end += phases_limit
    # First
    elif end <= 64:
        init = end
        end += phases_limit
    else:
        return (-1, -1, -1)
    return (init, end, phases_limit)
