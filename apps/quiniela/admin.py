from django.contrib import admin

from .models import Team, Game, Tournament, Quiniela

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Tournament)
admin.site.register(Quiniela)