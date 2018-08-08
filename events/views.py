import pandas as pd
from django.shortcuts import render
from models import Events, Leaderboard, GolfCourse
from django.db.models import F
# Create your views here.
def index(request):
        events = Events.objects.all()[:10]

        context = {
                'events': events
        }
	return render(request, 'events/index.html', context)

def leaderboard(request, id):
    event = Events.objects.get(id=id)
    golfcourse = event.title
    leaderboard = Leaderboard.objects.filter(event__id=id)
    output = ''
    front_par = golfcourse.hole1par + golfcourse.hole2par + golfcourse.hole3par + golfcourse.hole4par + golfcourse.hole5par + golfcourse.hole6par + golfcourse.hole7par + golfcourse.hole8par + golfcourse.hole9par
    back_par = golfcourse.hole10par + golfcourse.hole11par + golfcourse.hole12par + golfcourse.hole13par + golfcourse.hole14par + golfcourse.hole15par + golfcourse.hole16par + golfcourse.hole17par + golfcourse.hole18par
    total_par = front_par + back_par
    arr = []
    for i in leaderboard:
        name = "<td>" + str(i.name) + "</td>"
        hole1 = "<td>" + str(i.hole1score) + "</td>"
        hole2 = "<td>" + str(i.hole2score) + "</td>"
        hole3 = "<td>" + str(i.hole3score) + "</td>"
        hole4 = "<td>" + str(i.hole4score) + "</td>"
        hole5 = "<td>" + str(i.hole5score) + "</td>"
        hole6 = "<td>" + str(i.hole6score) + "</td>"
        hole7 = "<td>" + str(i.hole7score) + "</td>"
        hole8 = "<td>" + str(i.hole8score) + "</td>"
        hole9 = "<td>" + str(i.hole9score) + "</td>"
        out_total = i.hole1score + i.hole2score + i.hole3score + i.hole4score + i.hole5score + i.hole6score + i.hole7score + i.hole8score + i.hole9score
	out_score = "<td>" + str(out_total) + "</td>"
        front = hole1 + hole2 + hole3 + hole4 + hole5 + hole6 + hole7 + hole8 + hole9 + out_score
        hole10 = "<td>" + str(i.hole10score) + "</td>"
        hole11 = "<td>" + str(i.hole11score) + "</td>"
        hole12 = "<td>" + str(i.hole12score) + "</td>"
        hole13 = "<td>" + str(i.hole13score) + "</td>"
        hole14 = "<td>" + str(i.hole14score) + "</td>"
        hole15 = "<td>" + str(i.hole15score) + "</td>"
        hole16 = "<td>" + str(i.hole16score) + "</td>"
        hole17 = "<td>" + str(i.hole17score) + "</td>"
        hole18 = "<td>" + str(i.hole18score) + "</td>"
        in_total = i.hole10score + i.hole11score + i.hole12score + i.hole13score + i.hole14score + i.hole15score + i.hole16score + i.hole17score + i.hole18score
        in_score = "<td>" + str(in_total) + "</td>"
        back = hole10 + hole11 + hole12 + hole13 + hole14 + hole15 + hole16 + hole17 + hole18 + in_score
        total = "<td>" + str(out_total + in_total) + "</td>"
        row = "<tr>" + name + front + back + total + "</tr>"
        arr.append([in_total + out_total,row])
    #sort the leaderboard
    arr.sort(key=lambda x: x[0])
    for line in arr:
        output += line[1]
    context = {
            'front_par': front_par,
            'back_par': back_par,
            'total_par': total_par,
            'event': event,
            'leaderboard': leaderboard,
            'golfcourse': golfcourse,
            'output': output
    }
    return render(request, 'events/leaderboard.html', context)
