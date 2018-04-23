import json
from django.shortcuts import render
from django.utils.safestring import mark_safe

def index(request):
    return render(request, 'chat_index.html', {})

def room(request, room_name):
    return render(request, 'chat_room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })