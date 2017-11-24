# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from ..users.models import Profile, ProfileRequest


class ApiEndpoint(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, OAuth2!'})


# Return users that has a username, email, email or last name like the string passed
def users_like(request, like):
    # Search profiles with usersnames or mails like like
    q1 = Profile.objects.filter(user__username__icontains=like)
    q2 = Profile.objects.filter(user__email__icontains=like)
    q3 = Profile.objects.filter(user__name__icontains=like)

    # Join those querysets
    profiles = q1.union(q2, q3)

    return JsonResponse({'user': str(profiles)})


# Add a friend to the user in the request
class User2UserRequest(View):
    # Post requests only
    def post(self, request):
        # Get the user whos making the request and the request type
        request_t = request.POST.get('request_type', None)
        to_user = get_object_or_404(
            User,
            username=request.POST.get('username', None)
        )

        # Check if they're already friends, the request has been sent already or if a request is needed
        if request.user.profile.check_if_friends(to_user) and request_t == 'FR':
            return JsonResponse({'message': to_user.username + ' is already a Friend.'}, status=500)
        elif to_user.profile.get_if_request_from_user(request.user.profile, request_t):
            return JsonResponse({'message': 'Request to ' + to_user.username + ' is already sent.'}, status=500)
        elif to_user.profile.check_if_follower(request.user.profile) and request_t == 'FL':
            return JsonResponse({'message': 'You already follow ' + to_user.username + '.'}, status=500)
        elif request_t not in ['FR', 'FL']:
            return JsonResponse({'error': 'Bad user request.'}, status=500)
        else:
            # Create Friend Request
            try:
                p_request = ProfileRequest(
                    from_user=request.user.profile,
                    sugested_user=to_user.profile,
                    reason=request_t
                )
                # Save request and add it to targe user requests
                p_request.save()
                to_user.profile.requests.add(p_request)
                return JsonResponse({'message': request_t + ' request sent to ' + to_user.username + '.'}, status=200)
            # Catch and send the exception
            except Exception as e:
                return JsonResponse({'message': 'Exception: ' + str(e)}, status=500)


# Return all pending requests
class ReturnRequests(View):
    # post requests only
    def post(self, request):
        # Get all the requests from the user authorized
        return JsonResponse({'requests': request.user.profile.requests})


# Add a friend to the user in the request
class ConfirmRequest(View):
    # Post requests only
    def post(self, request):
        # Get the user whos making the request and the request type
        request_t = request.POST.get('request_type', None)
        from_user = get_object_or_404(
            User,
            username=request.POST.get('username', None)
        )

        user_request = request.user.profile.get_if_request_from_user(from_user.profile, request_t)
        print(request_t)
        print(from_user.profile)
        # Check if they're already friends, the request has been sent already or if a request is needed
        if user_request:
            user_request = user_request[0]
            try:
                if request_t == 'FR':
                    from_user.profile.friends.add(request.user.profile)
                    request.user.profile.friends.add(from_user.profile)
                    user_request.status = '0'
                    user_request.save()
                    return JsonResponse({'message': 'You and ' + from_user.username + ' are friends!'}, status=200)
                elif request_t == 'FL':
                    from_user.profile.following.add(request.user.profile)
                    request.user.profile.followers.add(from_user.profile)
                    user_request.status = '0'
                    user_request.save()
                    return JsonResponse({'message': from_user.username + ' is now following you!'}, status=200)
                else:
                    return JsonResponse({'message': 'Invalid request.'}, status=500)
            except Exception as e:
                return JsonResponse({'message': 'Exception: ' + str(e)}, status=500)
        else:
            return JsonResponse({'message': 'There is no previous request from ' + from_user.username + '.'}, status=500)

            