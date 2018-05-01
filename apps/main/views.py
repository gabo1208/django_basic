# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def home(request):
    #return render(request, 'home.html', context={'msg': "Hello, you!. You're at home."})
    return redirect('quiniela:user_quinielas')
