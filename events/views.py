from django.shortcuts import render
from models import Events
# Create your views here.
def index(request):
        events = Events.objects.all()[:10]

        context = {
                'events': events
        }
	return render(request, 'events/index.html', context)


def leaderboard(request, id):
    event = Events.objects.get(id=id)
    context = {
            'event': event
    }
    return render(request, 'events/leaderboard.html', context)
