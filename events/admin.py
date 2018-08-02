from django.contrib import admin

# Register your models here.
from .models import Events, Leaderboard, Tee, GolfCourse, Player

admin.site.register(Events)
admin.site.register(Leaderboard)
admin.site.register(Tee)
admin.site.register(GolfCourse)
admin.site.register(Player)
