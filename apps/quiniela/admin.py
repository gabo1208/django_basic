from django.contrib import admin

from .models import *

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(GameContext)
admin.site.register(GameResult)
admin.site.register(MemberFixture)
admin.site.register(Tournament)
admin.site.register(Quiniela)