# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from users.models import Profile


def users_like(request, like):
    # Search profiles with usersnames or mails like like
    q1 = Profile.objects.filter(user__username__icontains=like)
    q2 = Profile.objects.filter(user__email__icontains=like)
    q3 = Profile.objects.filter(user__name__icontains=like)

    # Join those querysets
    profiles = q1.union(q2, q3)

    return JsonResponse({'user': str(profiles)})
