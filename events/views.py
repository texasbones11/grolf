from django.shortcuts import render, redirect
from models import Events, Leaderboard, GolfCourse
from django.db.models import F
from forms import ScorecardForm
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

# Create your views here.
def index(request):
        events = Events.objects.all().order_by('-date')[:10]

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
    cell_start = "<td>"
    cell_highlight = "<td class=table-success>"
    cell_end = "</td>"
    skins1, skins2, skins3, skins4, skins5, skins6, skins7, skins8, skins9, skins10, skins11, skins12, skins13, skins14, skins15, skins16, skins17, skins18 = ([] for i in range(18))
    for i in leaderboard:
        name = str(i.name)
        if i.hole1score != 0:
            skins1.append([name,i.hole1score])
	if i.hole2score != 0:
            skins2.append([name,i.hole2score])
	if i.hole3score != 0:
            skins3.append([name,i.hole3score])
	if i.hole4score != 0:
            skins4.append([name,i.hole4score])
	if i.hole5score != 0:
            skins5.append([name,i.hole5score])
	if i.hole6score != 0:
            skins6.append([name,i.hole6score])
	if i.hole7score != 0:
            skins7.append([name,i.hole7score])
	if i.hole8score != 0:
            skins8.append([name,i.hole8score])
	if i.hole9score != 0:
            skins9.append([name,i.hole9score])
	if i.hole10score != 0:
            skins10.append([name,i.hole10score])
	if i.hole11score != 0:
            skins11.append([name,i.hole11score])
	if i.hole12score != 0:
            skins12.append([name,i.hole12score])
	if i.hole13score != 0:
            skins13.append([name,i.hole13score])
	if i.hole14score != 0:
            skins14.append([name,i.hole14score])
	if i.hole15score != 0:
            skins15.append([name,i.hole15score])
	if i.hole16score != 0:
            skins16.append([name,i.hole16score])
	if i.hole17score != 0:
            skins17.append([name,i.hole17score])
	if i.hole18score != 0:
            skins18.append([name,i.hole18score])
    #sort all holes to find skins
    skins1.sort(key=lambda x: x[1])
    skins2.sort(key=lambda x: x[1])
    skins3.sort(key=lambda x: x[1])
    skins4.sort(key=lambda x: x[1])
    skins5.sort(key=lambda x: x[1])
    skins6.sort(key=lambda x: x[1])
    skins7.sort(key=lambda x: x[1])
    skins8.sort(key=lambda x: x[1])
    skins9.sort(key=lambda x: x[1])
    skins10.sort(key=lambda x: x[1])
    skins11.sort(key=lambda x: x[1])
    skins12.sort(key=lambda x: x[1])
    skins13.sort(key=lambda x: x[1])
    skins14.sort(key=lambda x: x[1])
    skins15.sort(key=lambda x: x[1])
    skins16.sort(key=lambda x: x[1])
    skins17.sort(key=lambda x: x[1])
    skins18.sort(key=lambda x: x[1])
    for i in leaderboard:
        tee = cell_start + str(i.tee.teecolor) + cell_end
        name = cell_start + str(i.name) + cell_end
        checkbox = '<td>'+'<label class="checkbox-inline"><input type ="checkbox" name="dl" value="'+str(i.name)+'"></label>'+'</td>'
	if i.hole1score == 0:
	    hole1 = cell_start + cell_end
        elif (len(skins1) == 1 and str(skins1[0][0]) == str(i.name)) or (len(skins1) > 1 and skins1[0][1] != skins1[1][1] and str(skins1[0][0]) == str(i.name)):
            hole1 = cell_highlight + str(i.hole1score) + cell_end
        else:
            hole1 = cell_start + str(i.hole1score) + cell_end
	if i.hole2score == 0:
	    hole2 = cell_start + cell_end
        elif (len(skins2) == 1 and str(skins2[0][0]) == str(i.name)) or (len(skins2) > 1 and skins2[0][1] != skins2[1][1] and str(skins2[0][0]) == str(i.name)):
            hole2 = cell_highlight + str(i.hole2score) + cell_end
        else:
            hole2 = cell_start + str(i.hole2score) + cell_end
	if i.hole3score == 0:
	    hole3 = cell_start + cell_end
        elif (len(skins3) == 1 and str(skins3[0][0]) == str(i.name)) or (len(skins3) > 1 and skins3[0][1] != skins3[1][1] and str(skins3[0][0]) == str(i.name)):
            hole3 = cell_highlight + str(i.hole3score) + cell_end
        else:
            hole3 = cell_start + str(i.hole3score) + cell_end
	if i.hole4score == 0:
	    hole4 = cell_start + cell_end
        elif (len(skins4) == 1 and str(skins4[0][0]) == str(i.name)) or (len(skins4) > 1 and skins4[0][1] != skins4[1][1] and str(skins4[0][0]) == str(i.name)):
            hole4 = cell_highlight + str(i.hole4score) + cell_end
        else:
            hole4 = cell_start + str(i.hole4score) + cell_end
	if i.hole5score == 0:
	    hole5 = cell_start + cell_end
        elif (len(skins5) == 1 and str(skins5[0][0]) == str(i.name)) or (len(skins5) > 1 and skins5[0][1] != skins5[1][1] and str(skins5[0][0]) == str(i.name)):
                hole5 = cell_highlight + str(i.hole5score) + cell_end
        else:
            hole5 = cell_start + str(i.hole5score) + cell_end
	if i.hole6score == 0:
	    hole6 = cell_start + cell_end
        elif (len(skins6) == 1 and str(skins6[0][0]) == str(i.name)) or (len(skins6) > 1 and skins6[0][1] != skins6[1][1] and str(skins6[0][0]) == str(i.name)):
            hole6 = cell_highlight + str(i.hole6score) + cell_end
        else:
            hole6 = cell_start + str(i.hole6score) + cell_end
	if i.hole7score == 0:
	    hole7 = cell_start + cell_end
        elif (len(skins7) == 1 and str(skins7[0][0]) == str(i.name)) or (len(skins7) > 1 and skins7[0][1] != skins7[1][1] and str(skins7[0][0]) == str(i.name)):
            hole7 = cell_highlight + str(i.hole7score) + cell_end
        else:
            hole7 = cell_start + str(i.hole7score) + cell_end
	if i.hole8score == 0:
	    hole8 = cell_start + cell_end
        elif (len(skins8) == 1 and str(skins8[0][0]) == str(i.name)) or (len(skins8) > 1 and skins8[0][1] != skins8[1][1] and str(skins8[0][0]) == str(i.name)):
            hole8 = cell_highlight + str(i.hole8score) + cell_end
        else:
            hole8 = cell_start + str(i.hole8score) + cell_end
	if i.hole9score == 0:
	    hole9 = cell_start + cell_end
        elif (len(skins9) == 1 and str(skins9[0][0]) == str(i.name)) or (len(skins9) > 1 and skins9[0][1] != skins9[1][1] and str(skins9[0][0]) == str(i.name)):
            hole9 = cell_highlight + str(i.hole9score) + cell_end
        else:
            hole9 = cell_start + str(i.hole9score) + cell_end
        out_total = i.hole1score + i.hole2score + i.hole3score + i.hole4score + i.hole5score + i.hole6score + i.hole7score + i.hole8score + i.hole9score
	out_score = cell_start + str(out_total) + cell_end
        front = hole1 + hole2 + hole3 + hole4 + hole5 + hole6 + hole7 + hole8 + hole9 + out_score
	if i.hole10score == 0:
	    hole10 = cell_start + cell_end
        elif (len(skins10) == 1 and str(skins10[0][0]) == str(i.name)) or (len(skins10) > 1 and skins10[0][1] != skins10[1][1] and str(skins10[0][0]) == str(i.name)):
            hole10 = cell_highlight + str(i.hole10score) + cell_end
        else:
            hole10 = cell_start + str(i.hole10score) + cell_end
	if i.hole11score == 0:
	    hole11 = cell_start + cell_end
        elif (len(skins11) == 1 and str(skins11[0][0]) == str(i.name)) or (len(skins11) > 1 and skins11[0][1] != skins11[1][1] and str(skins11[0][0]) == str(i.name)):
            hole11 = cell_highlight + str(i.hole11score) + cell_end
        else:
            hole11 = cell_start + str(i.hole11score) + cell_end
	if i.hole12score == 0:
	    hole12 = cell_start + cell_end
        elif (len(skins12) == 1 and str(skins12[0][0]) == str(i.name)) or (len(skins12) > 1 and skins12[0][1] != skins12[1][1] and str(skins12[0][0]) == str(i.name)):
            hole12 = cell_highlight + str(i.hole12score) + cell_end
        else:
            hole12 = cell_start + str(i.hole12score) + cell_end
	if i.hole13score == 0:
	    hole13 = cell_start + cell_end
        elif (len(skins13) == 1 and str(skins13[0][0]) == str(i.name)) or (len(skins13) > 1 and skins13[0][1] != skins13[1][1] and str(skins13[0][0]) == str(i.name)):
            hole13 = cell_highlight + str(i.hole13score) + cell_end
        else:
            hole13 = cell_start + str(i.hole13score) + cell_end
	if i.hole14score == 0:
	    hole14 = cell_start + cell_end
        elif (len(skins14) == 1 and str(skins14[0][0]) == str(i.name)) or (len(skins14) > 1 and skins14[0][1] != skins14[1][1] and str(skins14[0][0]) == str(i.name)):
            hole14 = cell_highlight + str(i.hole14score) + cell_end
        else:
            hole14 = cell_start + str(i.hole14score) + cell_end
	if i.hole15score == 0:
	    hole15 = cell_start + cell_end
        elif (len(skins15) == 1 and str(skins15[0][0]) == str(i.name)) or (len(skins15) > 1 and skins15[0][1] != skins15[1][1] and str(skins15[0][0]) == str(i.name)):
            hole15 = cell_highlight + str(i.hole15score) + cell_end
        else:
            hole15 = cell_start + str(i.hole15score) + cell_end
	if i.hole16score == 0:
	    hole16 = cell_start + cell_end
        elif (len(skins16) == 1 and str(skins16[0][0]) == str(i.name)) or (len(skins16) > 1 and skins16[0][1] != skins16[1][1] and str(skins16[0][0]) == str(i.name)):
            hole16 = cell_highlight + str(i.hole16score) + cell_end
        else:
            hole16 = cell_start + str(i.hole16score) + cell_end
	if i.hole17score == 0:
	    hole17 = cell_start + cell_end
        elif (len(skins17) == 1 and str(skins17[0][0]) == str(i.name)) or (len(skins17) > 1 and skins17[0][1] != skins17[1][1] and str(skins17[0][0]) == str(i.name)):
            hole17 = cell_highlight + str(i.hole17score) + cell_end
        else:
            hole17 = cell_start + str(i.hole17score) + cell_end
	if i.hole18score == 0:
	    hole18 = cell_start + cell_end
        elif (len(skins18) == 1 and str(skins18[0][0]) == str(i.name)) or (len(skins18) > 1 and skins18[0][1] != skins18[1][1] and str(skins18[0][0]) == str(i.name)):
            hole18 = cell_highlight + str(i.hole18score) + cell_end
        else:
            hole18 = cell_start + str(i.hole18score) + cell_end
        in_total = i.hole10score + i.hole11score + i.hole12score + i.hole13score + i.hole14score + i.hole15score + i.hole16score + i.hole17score + i.hole18score
        in_score = cell_start + str(in_total) + cell_end
        back = hole10 + hole11 + hole12 + hole13 + hole14 + hole15 + hole16 + hole17 + hole18 + in_score
        total = cell_start + str(out_total + in_total) + cell_end
        hdcp_adj = int(round(i.tee.teerating * i.name.handicap / i.tee.teeslope))
        hdcp = cell_start + str(hdcp_adj) + cell_end
        net = cell_start + str(out_total + in_total - hdcp_adj) + cell_end
        row = checkbox + name + tee + front + back + total + hdcp + net
        arr.append([in_total + out_total,row])
    #sort the leaderboard
    arr.sort(key=lambda x: x[0])
    rank = 1
    count = 0
    prev = 0
    for line in arr:
        count += 1
        if line[0] != prev:
            rank = count
        prev = line[0]
        output += '<tr>' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
    if request.method == 'POST':
        dlist = request.POST.getlist('dl')
        print(dlist)
        request.session['dl'] = dlist
        request.session['value'] = ""
        return redirect('/events/scorecard/'+ id)
    context = {
            'front_par': front_par,
            'back_par': back_par,
            'total_par': total_par,
            'event': event,
            'leaderboard': leaderboard,
            'golfcourse': golfcourse,
            'output_gross': output,
            'output_net': output,
    }
    return render(request, 'events/leaderboard.html', context)

def scorecard(request, id):
    next_page = request.session['value']
    eventid = id
    event = Events.objects.get(id=id)
    leaderboard = Leaderboard.objects.filter(event__id=id)
    z = request.session['dl']
    loaded_list = [] 
    tester = leaderboard.values('id', 'name')
    selected_leaders = Leaderboard.objects.filter(name__name__in=z)
    for guy in z:
        man = list(Leaderboard.objects.filter(name__name=guy).values('id', 'name'))
        loaded_list += man
    print(len(loaded_list))
    for x in range(len(loaded_list)):
        print("test")
        print(loaded_list[x]['name'])
    SCFormset = modelformset_factory(Leaderboard, fields=('id','name','hole1score','hole2score','hole3score','hole4score', 'hole5score', 'hole6score', 'hole7score', 'hole8score','hole9score','hole10score','hole11score','hole12score', 'hole13score','hole14score','hole15score','hole16score', 'hole17score', 'hole18score'), extra=0)
    if request.method == 'POST':
        next_page = request.POST.get('value')
        request.session['value'] = next_page
        formset = SCFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                page = form.save(commit=False)
                page.event = event
                page.save()
            if 'leaderboard' in request.POST:
                url = '/events/leaderboard/' + str(eventid)
            else:
                url = '/events/scorecard'+str(next_page)+'/' + str(eventid)
            return redirect(url)
    else:
        formset = SCFormset(initial=[{'id': loaded_list[x]['id'],'name': loaded_list[x]['name']} for x in range(len(loaded_list))], queryset=selected_leaders)
    return render(request, 'events/scorecard'+str(next_page)+'.html', {'formset': formset, 'eventid': eventid})

def useradmin(request):
    context = "test"
    return render(request, "events/useradmin.html", {'context': context})
