from django.contrib import admin

# Register your models here.
from .models import Events, Handicap, Leaderboard, Tee, GolfCourse, TeamLeaderboard

admin.site.register(GolfCourse)
admin.site.register(Tee)
admin.site.register(Handicap)
admin.site.register(Events)
admin.site.register(Leaderboard)
admin.site.register(TeamLeaderboard)
