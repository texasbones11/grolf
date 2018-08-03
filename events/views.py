from django.shortcuts import render
from models import Events, Leaderboard, GolfCourse
# Create your views here.
def index(request):
        events = Events.objects.all()[:10]

        context = {
                'events': events
        }
	return render(request, 'events/index.html', context)


def leaderboard(request, id):
    event = Events.objects.get(id=id)
    golfcourse = GolfCourse.objects.all()[0]
    leaderboard = Leaderboard.objects.all()
    context = {
            'event': event,
            'leaderboard': leaderboard,
            'golfcourse': golfcourse
    }
    return render(request, 'events/leaderboard.html', context)
