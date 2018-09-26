from django.shortcuts import render, redirect
from models import Events, Leaderboard, GolfCourse, TeamLeaderboard
from django.db.models import F
from forms import ScorecardForm
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

# Create your views here.
def index(request):
        events = Events.objects.all().order_by('-date')[:6]

        context = {
                'events': events

        }
	return render(request, 'events/index.html', context)

def leaderboard(request, id):
    event = Events.objects.get(id=id)
    golfcourse = event.title
    leaderboard = Leaderboard.objects.filter(event__id=id)
    teamleaderboard = TeamLeaderboard.objects.filter(event__id=id)
    teamscoring = event.teamscoring
    netscoring = event.netscoring
    output = ''
    g_output = ''
    bb_output = ''
    front_par = golfcourse.hole1par + golfcourse.hole2par + golfcourse.hole3par + golfcourse.hole4par + golfcourse.hole5par + golfcourse.hole6par + golfcourse.hole7par + golfcourse.hole8par + golfcourse.hole9par
    back_par = golfcourse.hole10par + golfcourse.hole11par + golfcourse.hole12par + golfcourse.hole13par + golfcourse.hole14par + golfcourse.hole15par + golfcourse.hole16par + golfcourse.hole17par + golfcourse.hole18par
    total_par = front_par + back_par
    arr = []
    g_arr = []
    bb_arr = []
    cell_start = "<td>"
    cell_highlight_green = "<td class=table-success>"
    cell_highlight_yellow = "<td class=table-warning>"
    cell_end = "</td>"

    skins1, skins2, skins3, skins4, skins5, skins6, skins7, skins8, skins9, skins10, skins11, skins12, skins13, skins14, skins15, skins16, skins17, skins18 = ([] for i in range(18))
    for i in leaderboard:
        name = str(i.name)
	if i.skinsgross:
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
	over_total = 0
	finished_flag = 1
	front_finished_flag = 1
        back_finished_flag = 1
        tee = cell_start + str(i.tee.teecolor) + cell_end
        name = cell_start + str(i.name) + cell_end
        if event.lock:
            checkbox = ''
        else:
            checkbox = '<td>'+'<label class="checkbox-inline"><input type ="checkbox" name="dl" value="'+str(i.name)+'"></label>'+'</td>'
	if i.hole1score == 0:
	    hole1 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins1) == 1 and str(skins1[0][0]) == str(i.name)) or (len(skins1) > 1 and skins1[0][1] != skins1[1][1] and str(skins1[0][0]) == str(i.name)):
            hole1 = cell_highlight_green + str(i.hole1score) + cell_end
	    over_total += i.hole1score - golfcourse.hole1par
        else:
            hole1 = cell_start + str(i.hole1score) + cell_end
	    over_total += i.hole1score - golfcourse.hole1par
	if i.hole2score == 0:
	    hole2 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins2) == 1 and str(skins2[0][0]) == str(i.name)) or (len(skins2) > 1 and skins2[0][1] != skins2[1][1] and str(skins2[0][0]) == str(i.name)):
            hole2 = cell_highlight_green + str(i.hole2score) + cell_end
	    over_total += i.hole2score - golfcourse.hole2par
        else:
            hole2 = cell_start + str(i.hole2score) + cell_end
	    over_total += i.hole2score - golfcourse.hole2par
	if i.hole3score == 0:
	    hole3 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins3) == 1 and str(skins3[0][0]) == str(i.name)) or (len(skins3) > 1 and skins3[0][1] != skins3[1][1] and str(skins3[0][0]) == str(i.name)):
            hole3 = cell_highlight_green + str(i.hole3score) + cell_end
	    over_total += i.hole3score - golfcourse.hole3par
        else:
            hole3 = cell_start + str(i.hole3score) + cell_end
	    over_total += i.hole3score - golfcourse.hole3par
	if i.hole4score == 0:
	    hole4 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins4) == 1 and str(skins4[0][0]) == str(i.name)) or (len(skins4) > 1 and skins4[0][1] != skins4[1][1] and str(skins4[0][0]) == str(i.name)):
            hole4 = cell_highlight_green + str(i.hole4score) + cell_end
	    over_total += i.hole4score - golfcourse.hole4par
        else:
            hole4 = cell_start + str(i.hole4score) + cell_end
	    over_total += i.hole4score - golfcourse.hole4par
	if i.hole5score == 0:
	    hole5 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins5) == 1 and str(skins5[0][0]) == str(i.name)) or (len(skins5) > 1 and skins5[0][1] != skins5[1][1] and str(skins5[0][0]) == str(i.name)):
            hole5 = cell_highlight_green + str(i.hole5score) + cell_end
	    over_total += i.hole5score - golfcourse.hole5par
        else:
            hole5 = cell_start + str(i.hole5score) + cell_end
	    over_total += i.hole5score - golfcourse.hole5par
	if i.hole6score == 0:
	    hole6 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins6) == 1 and str(skins6[0][0]) == str(i.name)) or (len(skins6) > 1 and skins6[0][1] != skins6[1][1] and str(skins6[0][0]) == str(i.name)):
            hole6 = cell_highlight_green + str(i.hole6score) + cell_end
	    over_total += i.hole6score - golfcourse.hole6par
        else:
            hole6 = cell_start + str(i.hole6score) + cell_end
	    over_total += i.hole6score - golfcourse.hole6par
	if i.hole7score == 0:
	    hole7 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins7) == 1 and str(skins7[0][0]) == str(i.name)) or (len(skins7) > 1 and skins7[0][1] != skins7[1][1] and str(skins7[0][0]) == str(i.name)):
            hole7 = cell_highlight_green + str(i.hole7score) + cell_end
	    over_total += i.hole7score - golfcourse.hole7par
        else:
            hole7 = cell_start + str(i.hole7score) + cell_end
	    over_total += i.hole7score - golfcourse.hole7par
	if i.hole8score == 0:
	    hole8 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins8) == 1 and str(skins8[0][0]) == str(i.name)) or (len(skins8) > 1 and skins8[0][1] != skins8[1][1] and str(skins8[0][0]) == str(i.name)):
            hole8 = cell_highlight_green + str(i.hole8score) + cell_end
	    over_total += i.hole8score - golfcourse.hole8par
        else:
            hole8 = cell_start + str(i.hole8score) + cell_end
	    over_total += i.hole8score - golfcourse.hole8par
	if i.hole9score == 0:
	    hole9 = cell_start + cell_end
	    finished_flag = 0
	    front_finished_flag = 0
        elif (len(skins9) == 1 and str(skins9[0][0]) == str(i.name)) or (len(skins9) > 1 and skins9[0][1] != skins9[1][1] and str(skins9[0][0]) == str(i.name)):
            hole9 = cell_highlight_green + str(i.hole9score) + cell_end
	    over_total += i.hole9score - golfcourse.hole9par
        else:
            hole9 = cell_start + str(i.hole9score) + cell_end
	    over_total += i.hole9score - golfcourse.hole9par
	if i.hole10score == 0:
	    hole10 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins10) == 1 and str(skins10[0][0]) == str(i.name)) or (len(skins10) > 1 and skins10[0][1] != skins10[1][1] and str(skins10[0][0]) == str(i.name)):
            hole10 = cell_highlight_green + str(i.hole10score) + cell_end
	    over_total += i.hole10score - golfcourse.hole10par
        else:
            hole10 = cell_start + str(i.hole10score) + cell_end
	    over_total += i.hole10score - golfcourse.hole10par
	if i.hole11score == 0:
	    hole11 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins11) == 1 and str(skins11[0][0]) == str(i.name)) or (len(skins11) > 1 and skins11[0][1] != skins11[1][1] and str(skins11[0][0]) == str(i.name)):
            hole11 = cell_highlight_green + str(i.hole11score) + cell_end
	    over_total += i.hole11score - golfcourse.hole11par
        else:
            hole11 = cell_start + str(i.hole11score) + cell_end
	    over_total += i.hole11score - golfcourse.hole11par
	if i.hole12score == 0:
	    hole12 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins12) == 1 and str(skins12[0][0]) == str(i.name)) or (len(skins12) > 1 and skins12[0][1] != skins12[1][1] and str(skins12[0][0]) == str(i.name)):
            hole12 = cell_highlight_green + str(i.hole12score) + cell_end
	    over_total += i.hole12score - golfcourse.hole12par
        else:
            hole12 = cell_start + str(i.hole12score) + cell_end
	    over_total += i.hole12score - golfcourse.hole12par
	if i.hole13score == 0:
	    hole13 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins13) == 1 and str(skins13[0][0]) == str(i.name)) or (len(skins13) > 1 and skins13[0][1] != skins13[1][1] and str(skins13[0][0]) == str(i.name)):
            hole13 = cell_highlight_green + str(i.hole13score) + cell_end
	    over_total += i.hole13score - golfcourse.hole13par
        else:
            hole13 = cell_start + str(i.hole13score) + cell_end
	    over_total += i.hole13score - golfcourse.hole13par
	if i.hole14score == 0:
	    hole14 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins14) == 1 and str(skins14[0][0]) == str(i.name)) or (len(skins14) > 1 and skins14[0][1] != skins14[1][1] and str(skins14[0][0]) == str(i.name)):
            hole14 = cell_highlight_green + str(i.hole14score) + cell_end
	    over_total += i.hole14score - golfcourse.hole14par
        else:
            hole14 = cell_start + str(i.hole14score) + cell_end
	    over_total += i.hole14score - golfcourse.hole14par
	if i.hole15score == 0:
	    hole15 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins15) == 1 and str(skins15[0][0]) == str(i.name)) or (len(skins15) > 1 and skins15[0][1] != skins15[1][1] and str(skins15[0][0]) == str(i.name)):
            hole15 = cell_highlight_green + str(i.hole15score) + cell_end
	    over_total += i.hole15score - golfcourse.hole15par
        else:
            hole15 = cell_start + str(i.hole15score) + cell_end
	    over_total += i.hole15score - golfcourse.hole15par
	if i.hole16score == 0:
	    hole16 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins16) == 1 and str(skins16[0][0]) == str(i.name)) or (len(skins16) > 1 and skins16[0][1] != skins16[1][1] and str(skins16[0][0]) == str(i.name)):
            hole16 = cell_highlight_green + str(i.hole16score) + cell_end
	    over_total += i.hole16score - golfcourse.hole16par
        else:
            hole16 = cell_start + str(i.hole16score) + cell_end
	    over_total += i.hole16score - golfcourse.hole16par
	if i.hole17score == 0:
	    hole17 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins17) == 1 and str(skins17[0][0]) == str(i.name)) or (len(skins17) > 1 and skins17[0][1] != skins17[1][1] and str(skins17[0][0]) == str(i.name)):
            hole17 = cell_highlight_green + str(i.hole17score) + cell_end
	    over_total += i.hole17score - golfcourse.hole17par
        else:
            hole17 = cell_start + str(i.hole17score) + cell_end
	    over_total += i.hole17score - golfcourse.hole17par
	if i.hole18score == 0:
	    hole18 = cell_start + cell_end
	    finished_flag = 0
	    back_finished_flag = 0
        elif (len(skins18) == 1 and str(skins18[0][0]) == str(i.name)) or (len(skins18) > 1 and skins18[0][1] != skins18[1][1] and str(skins18[0][0]) == str(i.name)):
            hole18 = cell_highlight_green + str(i.hole18score) + cell_end
	    over_total += i.hole18score - golfcourse.hole18par
        else:
            hole18 = cell_start + str(i.hole18score) + cell_end
	    over_total += i.hole18score - golfcourse.hole18par
        out_total = i.hole1score + i.hole2score + i.hole3score + i.hole4score + i.hole5score + i.hole6score + i.hole7score + i.hole8score + i.hole9score
	if front_finished_flag == 0:
	    out_score = cell_start + cell_end
	else:
	    out_score = cell_start + str(out_total) + cell_end
        front = hole1 + hole2 + hole3 + hole4 + hole5 + hole6 + hole7 + hole8 + hole9 + out_score
        in_total = i.hole10score + i.hole11score + i.hole12score + i.hole13score + i.hole14score + i.hole15score + i.hole16score + i.hole17score + i.hole18score
	if back_finished_flag == 0:
            in_score = cell_start + cell_end
	else:
            in_score = cell_start + str(in_total) + cell_end
        back = hole10 + hole11 + hole12 + hole13 + hole14 + hole15 + hole16 + hole17 + hole18 + in_score
	if finished_flag == 1:
            if over_total < 0:
                total = '<td class="text-danger">' + str(out_total + in_total) + cell_end
            else:
                total = cell_start + str(out_total + in_total) + cell_end
        elif over_total > 0:
	    total = cell_start + "+" + str(over_total) + cell_end
        elif over_total < 0:
	    total = '<td class="text-danger">' + str(over_total) + cell_end
	elif over_total == 0:
	    total = cell_start + "E" + cell_end
	hdcp_adj = int(round(i.tee.teeslope * i.name.handicap / 113))
        row = checkbox + name + tee + front + back + total
        arr.append([over_total,row,i.gross])
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
	if line[2]:
            output += '<tr>' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
	else:
	    output += '<tr class="table-secondary">' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'

    g_skins1, g_skins2, g_skins3, g_skins4, g_skins5, g_skins6, g_skins7, g_skins8, g_skins9, g_skins10, g_skins11, g_skins12, g_skins13, g_skins14, g_skins15, g_skins16, g_skins17, g_skins18 = ([] for i in range(18))
    for i in leaderboard:
        name = str(i.name)
	hdcp_adj = int(round(i.tee.teeslope * i.name.handicap / 113))
	score_adj = 0
	if i.skinsnet:
            if i.hole1score != 0:
	        score_adj = i.hole1score
	        if (hdcp_adj - 18) / golfcourse.hole1handicap >= 1:
		    score_adj = i.hole1score - 2
	        elif (hdcp_adj / golfcourse.hole1handicap) >= 1:
		    score_adj = i.hole1score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole1handicap) < 1:
		    score_adj = i.hole1score + 1
                g_skins1.append([name,score_adj])
            if i.hole2score != 0:
	        score_adj = i.hole2score
	        if (hdcp_adj - 18) / golfcourse.hole2handicap >= 1:
		    score_adj = i.hole2score - 2
	        elif (hdcp_adj / golfcourse.hole2handicap) >= 1:
		    score_adj = i.hole2score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole2handicap) < 1:
		    score_adj = i.hole2score + 1
                g_skins2.append([name,score_adj])
            if i.hole3score != 0:
	        score_adj = i.hole3score
	        if (hdcp_adj - 18) / golfcourse.hole3handicap >= 1:
		    score_adj = i.hole3score - 2
	        elif (hdcp_adj / golfcourse.hole3handicap) >= 1:
	       	    score_adj = i.hole3score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole3handicap) < 1:
		    score_adj = i.hole3score + 1
                g_skins3.append([name,score_adj])
            if i.hole4score != 0:
	        score_adj = i.hole4score
	        if (hdcp_adj - 18) / golfcourse.hole4handicap >= 1:
	       	    score_adj = i.hole4score - 2
	        elif (hdcp_adj / golfcourse.hole4handicap) >= 1:
		    score_adj = i.hole4score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole4handicap) < 1:
		    score_adj = i.hole4score + 1
                g_skins4.append([name,score_adj])
            if i.hole5score != 0:
	        score_adj = i.hole5score
	        if (hdcp_adj - 18) / golfcourse.hole5handicap >= 1:
		    score_adj = i.hole5score - 2
	        elif (hdcp_adj / golfcourse.hole5handicap) >= 1:
		    score_adj = i.hole5score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole5handicap) < 1:
		    score_adj = i.hole5score + 1
                g_skins5.append([name,score_adj])
            if i.hole6score != 0:
	        score_adj = i.hole6score
	        if (hdcp_adj - 18) / golfcourse.hole6handicap >= 1:
		    score_adj = i.hole6score - 2
	        elif (hdcp_adj / golfcourse.hole6handicap) >= 1:
		    score_adj = i.hole6score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole6handicap) < 1:
		    score_adj = i.hole6score + 1
                g_skins6.append([name,score_adj])
            if i.hole7score != 0:
	        score_adj = i.hole7score
	        if (hdcp_adj - 18) / golfcourse.hole7handicap >= 1:
		    score_adj = i.hole7score - 2
	        elif (hdcp_adj / golfcourse.hole7handicap) >= 1:
		    score_adj = i.hole7score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole7handicap) < 1:
	    	    score_adj = i.hole7score + 1
                g_skins7.append([name,score_adj])
            if i.hole8score != 0:
	        score_adj = i.hole8score
	        if (hdcp_adj - 18) / golfcourse.hole8handicap >= 1:
		    score_adj = i.hole8score - 2
	        elif (hdcp_adj / golfcourse.hole8handicap) >= 1:
		    score_adj = i.hole8score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole8handicap) < 1:
		    score_adj = i.hole8score + 1
                g_skins8.append([name,score_adj])
            if i.hole9score != 0:
	        score_adj = i.hole9score
	        if (hdcp_adj - 18) / golfcourse.hole9handicap >= 1:
		    score_adj = i.hole9score - 2
	        elif (hdcp_adj / golfcourse.hole9handicap) >= 1:
		    score_adj = i.hole9score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole9handicap) < 1:
		    score_adj = i.hole9score + 1
                g_skins9.append([name,score_adj])
            if i.hole10score != 0:
	        score_adj = i.hole10score
	        if (hdcp_adj - 18) / golfcourse.hole10handicap >= 1:
		    score_adj = i.hole10score - 2
	        elif (hdcp_adj / golfcourse.hole10handicap) >= 1:
		    score_adj = i.hole10score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole10handicap) < 1:
		    score_adj = i.hole10score + 1
                g_skins10.append([name,score_adj])
            if i.hole11score != 0:
	        score_adj = i.hole11score
	        if (hdcp_adj - 18) / golfcourse.hole11handicap >= 1:
		    score_adj = i.hole11score - 2
	        elif (hdcp_adj / golfcourse.hole11handicap) >= 1:
		    score_adj = i.hole11score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole11handicap) < 1:
		    score_adj = i.hole11score + 1
                g_skins11.append([name,score_adj])
            if i.hole12score != 0:
	        score_adj = i.hole12score
	        if (hdcp_adj - 18) / golfcourse.hole12handicap >= 1:
		    score_adj = i.hole12score - 2
	        elif (hdcp_adj / golfcourse.hole12handicap) >= 1:
		    score_adj = i.hole12score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole12handicap) < 1:
		    score_adj = i.hole12score + 1
                g_skins12.append([name,score_adj])
            if i.hole13score != 0:
	        score_adj = i.hole13score
	        if (hdcp_adj - 18) / golfcourse.hole13handicap >= 1:
		    score_adj = i.hole13score - 2
	        elif (hdcp_adj / golfcourse.hole13handicap) >= 1:
		    score_adj = i.hole13score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole13handicap) < 1:
		    score_adj = i.hole13score + 1
                g_skins13.append([name,score_adj])
            if i.hole14score != 0:
	        score_adj = i.hole14score
	        if (hdcp_adj - 18) / golfcourse.hole14handicap >= 1:
		    score_adj = i.hole14score - 2
	        elif (hdcp_adj / golfcourse.hole14handicap) >= 1:
		    score_adj = i.hole14score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole14handicap) < 1:
		    score_adj = i.hole14score + 1
                g_skins14.append([name,score_adj])
            if i.hole15score != 0:
	        score_adj = i.hole15score
	        if (hdcp_adj - 18) / golfcourse.hole15handicap >= 1:
		    score_adj = i.hole15score - 2
	        elif (hdcp_adj / golfcourse.hole15handicap) >= 1:
		    score_adj = i.hole15score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole15handicap) < 1:
		    score_adj = i.hole15score + 1
                g_skins15.append([name,score_adj])
            if i.hole16score != 0:
	        score_adj = i.hole16score
	        if (hdcp_adj - 18) / golfcourse.hole16handicap >= 1:
		    score_adj = i.hole16score - 2
	        elif (hdcp_adj / golfcourse.hole16handicap) >= 1:
		    score_adj = i.hole16score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole16handicap) < 1:
		    score_adj = i.hole16score + 1
                g_skins16.append([name,score_adj])
            if i.hole17score != 0:
	        score_adj = i.hole17score
	        if (hdcp_adj - 18) / golfcourse.hole17handicap >= 1:
		    score_adj = i.hole17score - 2
	        elif (hdcp_adj / golfcourse.hole17handicap) >= 1:
		    score_adj = i.hole17score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole17handicap) < 1:
		    score_adj = i.hole17score + 1
                g_skins17.append([name,score_adj])
            if i.hole18score != 0:
	        score_adj = i.hole18score
	        if (hdcp_adj - 18) / golfcourse.hole18handicap >= 1:
		    score_adj = i.hole18score - 2
	        elif (hdcp_adj / golfcourse.hole18handicap) >= 1:
		    score_adj = i.hole18score - 1
	        elif ((18 + hdcp_adj) / golfcourse.hole18handicap) < 1:
		    score_adj = i.hole18score + 1
                g_skins18.append([name,score_adj])
    #sort all holes to find skins
    g_skins1.sort(key=lambda x: x[1])
    g_skins2.sort(key=lambda x: x[1])
    g_skins3.sort(key=lambda x: x[1])
    g_skins4.sort(key=lambda x: x[1])
    g_skins5.sort(key=lambda x: x[1])
    g_skins6.sort(key=lambda x: x[1])
    g_skins7.sort(key=lambda x: x[1])
    g_skins8.sort(key=lambda x: x[1])
    g_skins9.sort(key=lambda x: x[1])
    g_skins10.sort(key=lambda x: x[1])
    g_skins11.sort(key=lambda x: x[1])
    g_skins12.sort(key=lambda x: x[1])
    g_skins13.sort(key=lambda x: x[1])
    g_skins14.sort(key=lambda x: x[1])
    g_skins15.sort(key=lambda x: x[1])
    g_skins16.sort(key=lambda x: x[1])
    g_skins17.sort(key=lambda x: x[1])
    g_skins18.sort(key=lambda x: x[1])
    for i in leaderboard:
	g_over_total = 0
	g_finished_flag = 1
	g_front_finished_flag = 1
	g_back_finished_flag = 1
        tee = cell_start + str(i.tee.teecolor) + cell_end
        name = cell_start + str(i.name) + cell_end
        checkbox = '<td>'+'<label class="checkbox-inline"><input type ="checkbox" name="dl" value="'+str(i.name)+'"></label>'+'</td>'
	hdcp_adj = int(round(i.tee.teeslope * i.name.handicap / 113))
        score_adj = i.hole1score
        if (hdcp_adj - 18) / golfcourse.hole1handicap >= 1:
	    score_adj = i.hole1score - 2
        elif (hdcp_adj / golfcourse.hole1handicap) >= 1:
	    score_adj = i.hole1score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole1handicap) < 1:
	    score_adj = i.hole1score + 1
	hole1_adj = score_adj
	if i.hole1score == 0:
	    g_hole1 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins1) == 1 and str(g_skins1[0][0]) == str(i.name)) or (len(g_skins1) > 1 and g_skins1[0][1] != g_skins1[1][1] and str(g_skins1[0][0]) == str(i.name)):
            g_hole1 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole1par
        else:
            g_hole1 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole1par
        score_adj = i.hole2score
        if (hdcp_adj - 18) / golfcourse.hole2handicap >= 1:
	    score_adj = i.hole2score - 2
        elif (hdcp_adj / golfcourse.hole2handicap) >= 1:
	    score_adj = i.hole2score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole2handicap) < 1:
	    score_adj = i.hole2score + 1
	hole2_adj = score_adj
	if i.hole2score == 0:
	    g_hole2 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins2) == 1 and str(g_skins2[0][0]) == str(i.name)) or (len(g_skins2) > 1 and g_skins2[0][1] != g_skins2[1][1] and str(g_skins2[0][0]) == str(i.name)):
            g_hole2 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole2par
        else:
            g_hole2 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole2par
        score_adj = i.hole3score
        if (hdcp_adj - 18) / golfcourse.hole3handicap >= 1:
	    score_adj = i.hole3score - 2
        elif (hdcp_adj / golfcourse.hole3handicap) >= 1:
	    score_adj = i.hole3score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole3handicap) < 1:
	    score_adj = i.hole3score + 1
	hole3_adj = score_adj
	if i.hole3score == 0:
	    g_hole3 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins3) == 1 and str(g_skins3[0][0]) == str(i.name)) or (len(g_skins3) > 1 and g_skins3[0][1] != g_skins3[1][1] and str(g_skins3[0][0]) == str(i.name)):
            g_hole3 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole3par
        else:
            g_hole3 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole3par
        score_adj = i.hole4score
        if (hdcp_adj - 18) / golfcourse.hole4handicap >= 1:
	    score_adj = i.hole4score - 2
        elif (hdcp_adj / golfcourse.hole4handicap) >= 1:
	    score_adj = i.hole4score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole4handicap) < 1:
	    score_adj = i.hole4score + 1
	hole4_adj = score_adj
	if i.hole4score == 0:
	    g_hole4 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins4) == 1 and str(g_skins4[0][0]) == str(i.name)) or (len(g_skins4) > 1 and g_skins4[0][1] != g_skins4[1][1] and str(g_skins4[0][0]) == str(i.name)):
            g_hole4 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole4par
        else:
            g_hole4 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole4par
        score_adj = i.hole5score
        if (hdcp_adj - 18) / golfcourse.hole5handicap >= 1:
	    score_adj = i.hole5score - 2
        elif (hdcp_adj / golfcourse.hole5handicap) >= 1:
	    score_adj = i.hole5score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole5handicap) < 1:
	    score_adj = i.hole5score + 1
	hole5_adj = score_adj
	if i.hole5score == 0:
	    g_hole5 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins5) == 1 and str(g_skins5[0][0]) == str(i.name)) or (len(g_skins5) > 1 and g_skins5[0][1] != g_skins5[1][1] and str(g_skins5[0][0]) == str(i.name)):
            g_hole5 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole5par
        else:
            g_hole5 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole5par
        score_adj = i.hole6score
        if (hdcp_adj - 18) / golfcourse.hole6handicap >= 1:
	    score_adj = i.hole6score - 2
        elif (hdcp_adj / golfcourse.hole6handicap) >= 1:
	    score_adj = i.hole6score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole6handicap) < 1:
	    score_adj = i.hole6score + 1
	hole6_adj = score_adj
	if i.hole6score == 0:
	    g_hole6 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins6) == 1 and str(g_skins6[0][0]) == str(i.name)) or (len(g_skins6) > 1 and g_skins6[0][1] != g_skins6[1][1] and str(g_skins6[0][0]) == str(i.name)):
            g_hole6 = cell_highlight_yellow + str(score_adj) + cell_end
            g_over_total += score_adj - golfcourse.hole6par
        else:
            g_hole6 = cell_start + str(score_adj) + cell_end
            g_over_total += score_adj - golfcourse.hole6par
        score_adj = i.hole7score
        if (hdcp_adj - 18) / golfcourse.hole7handicap >= 1:
	    score_adj = i.hole7score - 2
        elif (hdcp_adj / golfcourse.hole7handicap) >= 1:
	    score_adj = i.hole7score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole7handicap) < 1:
	    score_adj = i.hole7score + 1
	hole7_adj = score_adj
	if i.hole7score == 0:
	    g_hole7 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins7) == 1 and str(g_skins7[0][0]) == str(i.name)) or (len(g_skins7) > 1 and g_skins7[0][1] != g_skins7[1][1] and str(g_skins7[0][0]) == str(i.name)):
            g_hole7 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole7par
        else:
            g_hole7 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole7par
        score_adj = i.hole8score
        if (hdcp_adj - 18) / golfcourse.hole8handicap >= 1:
	    score_adj = i.hole8score - 2
        elif (hdcp_adj / golfcourse.hole8handicap) >= 1:
	    score_adj = i.hole8score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole8handicap) < 1:
	    score_adj = i.hole8score + 1
	hole8_adj = score_adj
	if i.hole8score == 0:
	    g_hole8 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins8) == 1 and str(g_skins8[0][0]) == str(i.name)) or (len(g_skins8) > 1 and g_skins8[0][1] != g_skins8[1][1] and str(g_skins8[0][0]) == str(i.name)):
            g_hole8 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole8par
        else:
            g_hole8 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole8par
        score_adj = i.hole9score
        if (hdcp_adj - 18) / golfcourse.hole9handicap >= 1:
	    score_adj = i.hole9score - 2
        elif (hdcp_adj / golfcourse.hole9handicap) >= 1:
	    score_adj = i.hole9score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole9handicap) < 1:
	    score_adj = i.hole9score + 1
	hole9_adj = score_adj
	if i.hole9score == 0:
	    g_hole9 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins9) == 1 and str(g_skins9[0][0]) == str(i.name)) or (len(g_skins9) > 1 and g_skins9[0][1] != g_skins9[1][1] and str(g_skins9[0][0]) == str(i.name)):
            g_hole9 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole9par
        else:
            g_hole9 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole9par
        score_adj = i.hole10score
        if (hdcp_adj - 18) / golfcourse.hole10handicap >= 1:
	    score_adj = i.hole10score - 2
        elif (hdcp_adj / golfcourse.hole10handicap) >= 1:
	    score_adj = i.hole10score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole10handicap) < 1:
	    score_adj = i.hole10score + 1
	hole10_adj = score_adj
	if i.hole10score == 0:
	    g_hole10 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins10) == 1 and str(g_skins10[0][0]) == str(i.name)) or (len(g_skins10) > 1 and g_skins10[0][1] != g_skins10[1][1] and str(g_skins10[0][0]) == str(i.name)):
            g_hole10 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole10par
        else:
            g_hole10 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole10par
        score_adj = i.hole11score
        if (hdcp_adj - 18) / golfcourse.hole11handicap >= 1:
	    score_adj = i.hole11score - 2
        elif (hdcp_adj / golfcourse.hole11handicap) >= 1:
	    score_adj = i.hole11score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole11handicap) < 1:
	    score_adj = i.hole11score + 1
	hole11_adj = score_adj
	if i.hole11score == 0:
	    g_hole11 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins11) == 1 and str(g_skins11[0][0]) == str(i.name)) or (len(g_skins11) > 1 and g_skins11[0][1] != g_skins11[1][1] and str(g_skins11[0][0]) == str(i.name)):
            g_hole11 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole11par
        else:
            g_hole11 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole11par
        score_adj = i.hole12score
        if (hdcp_adj - 18) / golfcourse.hole12handicap >= 1:
	    score_adj = i.hole12score - 2
        elif (hdcp_adj / golfcourse.hole12handicap) >= 1:
	    score_adj = i.hole12score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole12handicap) < 1:
	    score_adj = i.hole12score + 1
	hole12_adj = score_adj
	if i.hole12score == 0:
	    g_hole12 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins12) == 1 and str(g_skins12[0][0]) == str(i.name)) or (len(g_skins12) > 1 and g_skins12[0][1] != g_skins12[1][1] and str(g_skins12[0][0]) == str(i.name)):
            g_hole12 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole12par
        else:
            g_hole12 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole12par
        score_adj = i.hole13score
        if (hdcp_adj - 18) / golfcourse.hole13handicap >= 1:
	    score_adj = i.hole13score - 2
        elif (hdcp_adj / golfcourse.hole13handicap) >= 1:
	    score_adj = i.hole13score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole13handicap) < 1:
	    score_adj = i.hole13score + 1
	hole13_adj = score_adj
	if i.hole13score == 0:
	    g_hole13 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins13) == 1 and str(g_skins13[0][0]) == str(i.name)) or (len(g_skins13) > 1 and g_skins13[0][1] != g_skins13[1][1] and str(g_skins13[0][0]) == str(i.name)):
            g_hole13 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole13par
        else:
            g_hole13 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole13par
        score_adj = i.hole14score
        if (hdcp_adj - 18) / golfcourse.hole14handicap >= 1:
	    score_adj = i.hole14score - 2
        elif (hdcp_adj / golfcourse.hole14handicap) >= 1:
	    score_adj = i.hole14score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole14handicap) < 1:
	    score_adj = i.hole14score + 1
	hole14_adj = score_adj
	if i.hole14score == 0:
	    g_hole14 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins14) == 1 and str(g_skins14[0][0]) == str(i.name)) or (len(g_skins14) > 1 and g_skins14[0][1] != g_skins14[1][1] and str(g_skins14[0][0]) == str(i.name)):
            g_hole14 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole14par
        else:
            g_hole14 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole14par
        score_adj = i.hole15score
        if (hdcp_adj - 18) / golfcourse.hole15handicap >= 1:
	    score_adj = i.hole15score - 2
        elif (hdcp_adj / golfcourse.hole15handicap) >= 1:
	    score_adj = i.hole15score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole15handicap) < 1:
	    score_adj = i.hole15score + 1
	hole15_adj = score_adj
	if i.hole15score == 0:
	    g_hole15 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins15) == 1 and str(g_skins15[0][0]) == str(i.name)) or (len(g_skins15) > 1 and g_skins15[0][1] != g_skins15[1][1] and str(g_skins15[0][0]) == str(i.name)):
            g_hole15 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole15par
        else:
            g_hole15 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole15par
        score_adj = i.hole16score
        if (hdcp_adj - 18) / golfcourse.hole16handicap >= 1:
	    score_adj = i.hole16score - 2
        elif (hdcp_adj / golfcourse.hole16handicap) >= 1:
	    score_adj = i.hole16score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole16handicap) < 1:
	    score_adj = i.hole16score + 1
	hole16_adj = score_adj
	if i.hole16score == 0:
	    g_hole16 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins16) == 1 and str(g_skins16[0][0]) == str(i.name)) or (len(g_skins16) > 1 and g_skins16[0][1] != g_skins16[1][1] and str(g_skins16[0][0]) == str(i.name)):
            g_hole16 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole16par
        else:
            g_hole16 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole16par
        score_adj = i.hole17score
        if (hdcp_adj - 18) / golfcourse.hole17handicap >= 1:
	    score_adj = i.hole17score - 2
        elif (hdcp_adj / golfcourse.hole17handicap) >= 1:
	    score_adj = i.hole17score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole17handicap) < 1:
	    score_adj = i.hole17score + 1
	hole17_adj = score_adj
	if i.hole17score == 0:
	    g_hole17 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins17) == 1 and str(g_skins17[0][0]) == str(i.name)) or (len(g_skins17) > 1 and g_skins17[0][1] != g_skins17[1][1] and str(g_skins17[0][0]) == str(i.name)):
            g_hole17 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole17par
        else:
            g_hole17 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole17par
        score_adj = i.hole18score
        if (hdcp_adj - 18) / golfcourse.hole18handicap >= 1:
	    score_adj = i.hole18score - 2
        elif (hdcp_adj / golfcourse.hole18handicap) >= 1:
	    score_adj = i.hole18score - 1
        elif ((18 + hdcp_adj) / golfcourse.hole18handicap) < 1:
	    score_adj = i.hole18score + 1
	hole18_adj = score_adj
	if i.hole18score == 0:
	    g_hole18 = cell_start + cell_end
	    g_finished_flag = 0
	    g_back_finished_flag = 0
        elif (len(g_skins18) == 1 and str(g_skins18[0][0]) == str(i.name)) or (len(g_skins18) > 1 and g_skins18[0][1] != g_skins18[1][1] and str(g_skins18[0][0]) == str(i.name)):
            g_hole18 = cell_highlight_yellow + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole18par
        else:
            g_hole18 = cell_start + str(score_adj) + cell_end
	    g_over_total += score_adj - golfcourse.hole18par
        g_out_total = hole1_adj + hole2_adj + hole3_adj + hole4_adj + hole5_adj + hole6_adj + hole7_adj + hole8_adj + hole9_adj
	if g_front_finished_flag == 0:
	    g_out_score = cell_start + cell_end
	else:
	    g_out_score = cell_start + str(g_out_total) + cell_end
        g_front = g_hole1 + g_hole2 + g_hole3 + g_hole4 + g_hole5 + g_hole6 + g_hole7 + g_hole8 + g_hole9 + g_out_score
        g_in_total = hole10_adj + hole11_adj + hole12_adj + hole13_adj + hole14_adj + hole15_adj + hole16_adj + hole17_adj + hole18_adj
	if g_back_finished_flag == 0:
            g_in_score = cell_start + cell_end
	else:
            g_in_score = cell_start + str(g_in_total) + cell_end
        g_back = g_hole10 + g_hole11 + g_hole12 + g_hole13 + g_hole14 + g_hole15 + g_hole16 + g_hole17 + g_hole18 + g_in_score
	if g_finished_flag == 1:
            if g_over_total < 0:
                g_total = '<td class="text-danger">' + str(g_out_total + g_in_total) + cell_end
            else:
	        g_total = cell_start + str(g_out_total + g_in_total) + cell_end
        elif g_over_total > 0:
	    g_total = cell_start + "+" + str(g_over_total) + cell_end
        elif g_over_total < 0:
	    g_total = '<td class="text-danger">' + str(g_over_total) + cell_end
	elif g_over_total == 0:
	    g_total = cell_start + "E" + cell_end
	hdcp_adj = int(round(i.tee.teeslope * i.name.handicap / 113))
        hdcp = cell_start + str(hdcp_adj) + cell_end
        net = g_total
        row = hdcp + name + tee + g_front + g_back + net
        g_arr.append([g_over_total,row,i.net])
    #sort the leaderboard
    g_arr.sort(key=lambda x: x[0])
    rank = 1
    count = 0
    prev = 0
    for line in g_arr:
        count += 1
        if line[0] != prev:
            rank = count
        prev = line[0]
	if line[2]:
            g_output += '<tr>' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
	else:
            g_output += '<tr class="table-secondary">' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
    if request.method == 'POST':
        dlist = request.POST.getlist('dl')
        print(dlist)
        request.session['dl'] = dlist
        request.session['value'] = ""
        return redirect('/events/login/'+ id)
    for i in teamleaderboard:
	bb_finished_flag = 1
	bb_front_finished_flag = 1
	bb_back_finished_flag = 1
        teamscore = 0
        teamfront = 0
        teamback = 0
	bb_overtotal = 0
        bb_row = '<td>' + str(i.teamname) + '</td>'
        if i.player1.hole1score < i.player2.hole1score and i.player1.hole1score != 0 or i.player2.hole1score == 0:
	    bb_hole1 = i.player1.hole1score
        else:
	    bb_hole1 = i.player2.hole1score
	if bb_hole1 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole1 - golfcourse.hole1par
            bb_row += '<td>' + str(bb_hole1) + '</td>'
	teamscore += bb_hole1
        teamfront = teamscore
        if i.player1.hole2score < i.player2.hole2score and i.player1.hole2score != 0 or i.player2.hole2score == 0:
	    bb_hole2 = i.player1.hole2score
        else:
	    bb_hole2 = i.player2.hole2score
	if bb_hole2 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole2 - golfcourse.hole2par
            bb_row += '<td>' + str(bb_hole2) + '</td>'
	teamscore += bb_hole2
        teamfront = teamscore
        if i.player1.hole3score < i.player2.hole3score and i.player1.hole3score != 0 or i.player2.hole3score == 0:
	    bb_hole3 = i.player1.hole3score
        else:
	    bb_hole3 = i.player2.hole3score
	if bb_hole3 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole3 - golfcourse.hole3par
            bb_row += '<td>' + str(bb_hole3) + '</td>'
	teamscore += bb_hole3
        teamfront = teamscore
        if i.player1.hole4score < i.player2.hole4score and i.player1.hole4score != 0 or i.player2.hole4score == 0:
	    bb_hole4 = i.player1.hole4score
        else:
	    bb_hole4 = i.player2.hole4score
	if bb_hole4 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole4 - golfcourse.hole4par
            bb_row += '<td>' + str(bb_hole4) + '</td>'
	teamscore += bb_hole4
        teamfront = teamscore
        if i.player1.hole5score < i.player2.hole5score and i.player1.hole5score != 0 or i.player2.hole5score == 0:
	    bb_hole5 = i.player1.hole5score
        else:
	    bb_hole5 = i.player2.hole5score
	if bb_hole5 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole5 - golfcourse.hole5par
            bb_row += '<td>' + str(bb_hole5) + '</td>'
	teamscore += bb_hole5
        teamfront = teamscore
        if i.player1.hole6score < i.player2.hole6score and i.player1.hole6score != 0 or i.player2.hole6score == 0:
	    bb_hole6 = i.player1.hole6score
        else:
	    bb_hole6 = i.player2.hole6score
	if bb_hole6 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole6 - golfcourse.hole6par
            bb_row += '<td>' + str(bb_hole6) + '</td>'
	teamscore += bb_hole6
        teamfront = teamscore
        if i.player1.hole7score < i.player2.hole7score and i.player1.hole7score != 0 or i.player2.hole7score == 0:
	    bb_hole7 = i.player1.hole7score
        else:
	    bb_hole7 = i.player2.hole7score
	if bb_hole7 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole7 - golfcourse.hole7par
            bb_row += '<td>' + str(bb_hole7) + '</td>'
	teamscore += bb_hole7
        teamfront = teamscore
        if i.player1.hole8score < i.player2.hole8score and i.player1.hole8score != 0 or i.player2.hole8score == 0:
	    bb_hole8 = i.player1.hole8score
        else:
	    bb_hole8 = i.player2.hole8score
	if bb_hole8 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole8 - golfcourse.hole8par
            bb_row += '<td>' + str(bb_hole8) + '</td>'
	teamscore += bb_hole8
        teamfront = teamscore
        if i.player1.hole9score < i.player2.hole9score and i.player1.hole9score != 0 or i.player2.hole9score == 0:
	    bb_hole9 = i.player1.hole9score
        else:
	    bb_hole9 = i.player2.hole9score
	if bb_hole9 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole9 - golfcourse.hole9par
            bb_row += '<td>' + str(bb_hole9) + '</td>'
	teamscore += bb_hole9
        teamfront = teamscore
	if bb_front_finished_flag == 1:
            bb_row += '<td>' + str(teamfront) + '</td>'
	else:
	    bb_row += '<td></td>'
        if i.player1.hole10score < i.player2.hole10score and i.player1.hole10score != 0 or i.player2.hole10score == 0:
	    bb_hole10 = i.player1.hole10score
        else:
	    bb_hole10 = i.player2.hole10score
	if bb_hole10 == 0:
	    bb_finished_flag = 0
	    bb_front_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole10 - golfcourse.hole10par
            bb_row += '<td>' + str(bb_hole10) + '</td>'
	teamscore += bb_hole10
        teamback = teamscore - teamfront
        if i.player1.hole11score < i.player2.hole11score and i.player1.hole11score != 0 or i.player2.hole11score == 0:
	    bb_hole11 = i.player1.hole11score
        else:
	    bb_hole11 = i.player2.hole11score
	if bb_hole11 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole11 - golfcourse.hole11par
            bb_row += '<td>' + str(bb_hole11) + '</td>'
	teamscore += bb_hole11
        teamback = teamscore - teamfront
        if i.player1.hole12score < i.player2.hole12score and i.player1.hole12score != 0 or i.player2.hole12score == 0:
	    bb_hole12 = i.player1.hole12score
        else:
	    bb_hole12 = i.player2.hole12score
	if bb_hole12 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole12 - golfcourse.hole12par
            bb_row += '<td>' + str(bb_hole12) + '</td>'
	teamscore += bb_hole12
        teamback = teamscore - teamfront
        if i.player1.hole13score < i.player2.hole13score and i.player1.hole13score != 0 or i.player2.hole13score == 0:
	    bb_hole13 = i.player1.hole13score
        else:
	    bb_hole13 = i.player2.hole13score
	if bb_hole13 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole13 - golfcourse.hole13par
            bb_row += '<td>' + str(bb_hole13) + '</td>'
	teamscore += bb_hole13
        teamback = teamscore - teamfront
        if i.player1.hole14score < i.player2.hole14score and i.player1.hole14score != 0 or i.player2.hole14score == 0:
	    bb_hole14 = i.player1.hole14score
        else:
	    bb_hole14 = i.player2.hole14score
	if bb_hole14 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole14 - golfcourse.hole14par
            bb_row += '<td>' + str(bb_hole14) + '</td>'
	teamscore += bb_hole14
        teamback = teamscore - teamfront
        if i.player1.hole15score < i.player2.hole15score and i.player1.hole15score != 0 or i.player2.hole15score == 0:
	    bb_hole15 = i.player1.hole15score
        else:
	    bb_hole15 = i.player2.hole15score
	if bb_hole15 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole15 - golfcourse.hole15par
            bb_row += '<td>' + str(bb_hole15) + '</td>'
	teamscore += bb_hole15
        teamback = teamscore - teamfront
        if i.player1.hole16score < i.player2.hole16score and i.player1.hole16score != 0 or i.player2.hole16score == 0:
	    bb_hole16 = i.player1.hole16score
        else:
	    bb_hole16 = i.player2.hole16score
	if bb_hole16 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole16 - golfcourse.hole16par
            bb_row += '<td>' + str(bb_hole16) + '</td>'
	teamscore += bb_hole16
        teamback = teamscore - teamfront
        if i.player1.hole17score < i.player2.hole17score and i.player1.hole17score != 0 or i.player2.hole17score == 0:
	    bb_hole17 = i.player1.hole17score
        else:
	    bb_hole17 = i.player2.hole17score
	if bb_hole17 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
            bb_overtotal += bb_hole17 - golfcourse.hole17par
            bb_row += '<td>' + str(bb_hole17) + '</td>'
	teamscore += bb_hole17
        teamback = teamscore - teamfront
        if i.player1.hole18score < i.player2.hole18score and i.player1.hole18score != 0 or i.player2.hole18score == 0:
	    bb_hole18 = i.player1.hole18score
        else:
	    bb_hole18 = i.player2.hole18score
	if bb_hole18 == 0:
	    bb_finished_flag = 0
	    bb_back_finished_flag = 0
            bb_row += '<td></td>'
	else:
	    bb_overtotal += bb_hole18 - golfcourse.hole18par
            bb_row += '<td>' + str(bb_hole18) + '</td>'
	teamscore += bb_hole18
        teamback = teamscore - teamfront
	if bb_back_finished_flag == 1:
            bb_row += '<td>' + str(teamback) + '</td>'
	else:
	    bb_row += '<td></td>'
	if bb_finished_flag == 1:
            if bb_overtotal < 0:
                bb_row += '<td class="text-danger">' + str(teamscore) + '</td>'
            else:
	        bb_row += '<td>' + str(teamscore) + '</td>'
        elif bb_overtotal > 0:
	    bb_row += cell_start + "+" + str(bb_overtotal) + cell_end
        elif bb_overtotal < 0:
	    bb_row += '<td class="text-danger">' + str(bb_overtotal) + cell_end
	elif bb_overtotal == 0:
	    bb_row += cell_start + "E" + cell_end
        bb_arr.append([bb_overtotal,bb_row])
    #sort the leaderboard
    bb_arr.sort(key=lambda x: x[0])
    rank = 1
    count = 0
    prev = 0
    for line in bb_arr:
	count += 1
	if line[0] != prev:
	    rank = count
	prev = line[0]
	bb_output += '<tr>' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
    context = {
            'front_par': front_par,
            'back_par': back_par,
            'total_par': total_par,
            'event': event,
            'leaderboard': leaderboard,
            'golfcourse': golfcourse,
            'output_gross': output,
            'output_net': g_output,
            'output_bestball': bb_output,
            'netscoring': netscoring,
            'teamscoring': teamscoring,
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
    selected_leaders = leaderboard.filter(name__name__in=z)
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

def login(request, id):
    event = Events.objects.get(id=id)
    eventid = id
    context = "test"
    if request.method == 'POST':
        next_page = request.POST.get('value')
        request.session['value'] = next_page
        password = request.POST.get('inputpassword')
        if 'leaderboard' in request.POST:
            url = '/events/leaderboard/' + str(eventid)
        elif str(password) == str(event.password):
            url = '/events/scorecard'+str(next_page)+'/' + str(eventid)
            print("success")
        else:
            url = '/events/leaderboard/' + str(eventid)
            print(str(event.password) + " " + str(password))
            print(str(request.POST))
        return redirect(url)
    return render(request, "events/login.html", {'context': context})
