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
    g_output = ''
    front_par = golfcourse.hole1par + golfcourse.hole2par + golfcourse.hole3par + golfcourse.hole4par + golfcourse.hole5par + golfcourse.hole6par + golfcourse.hole7par + golfcourse.hole8par + golfcourse.hole9par
    back_par = golfcourse.hole10par + golfcourse.hole11par + golfcourse.hole12par + golfcourse.hole13par + golfcourse.hole14par + golfcourse.hole15par + golfcourse.hole16par + golfcourse.hole17par + golfcourse.hole18par
    total_par = front_par + back_par
    arr = []
    g_arr = []
    cell_start = "<td>"
    cell_highlight_green = "<td class=table-success>"
    cell_highlight_yellow = "<td class=table-warning>"
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
	over_total = 0
	finished_flag = 1
	front_finished_flag = 1
        tee = cell_start + str(i.tee.teecolor) + cell_end
        name = cell_start + str(i.name) + cell_end
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
	hdcp_adj = int(round(i.tee.teerating * i.name.handicap / i.tee.teeslope))
        row = checkbox + name + tee + front + back + total
        arr.append([over_total,row])
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

    g_skins1, g_skins2, g_skins3, g_skins4, g_skins5, g_skins6, g_skins7, g_skins8, g_skins9, g_skins10, g_skins11, g_skins12, g_skins13, g_skins14, g_skins15, g_skins16, g_skins17, g_skins18 = ([] for i in range(18))
    for i in leaderboard:
        name = str(i.name)
	hdcp_adj = int(round(i.tee.teerating * i.name.handicap / i.tee.teeslope))
	score_adj = 0
        if i.hole1score != 0:
	    score_adj = i.hole1score
	    if (hdcp_adj - 18) / golfcourse.hole1handicap >= 1:
		score_adj = i.hole1score - 2
	    elif (hdcp_adj / golfcourse.hole1handicap) >= 1:
		score_adj = i.hole1score - 1
	    elif (hdcp_adj / golfcourse.hole1handicap) <= -1:
		score_adj = i.hole1score + 1
            g_skins1.append([name,score_adj])
        if i.hole2score != 0:
	    score_adj = i.hole2score
	    if (hdcp_adj - 18) / golfcourse.hole2handicap >= 1:
		score_adj = i.hole2score - 2
	    elif (hdcp_adj / golfcourse.hole2handicap) >= 1:
		score_adj = i.hole2score - 1
	    elif (hdcp_adj / golfcourse.hole2handicap) <= -1:
		score_adj = i.hole2score + 1
            g_skins2.append([name,score_adj])
        if i.hole3score != 0:
	    score_adj = i.hole3score
	    if (hdcp_adj - 18) / golfcourse.hole3handicap >= 1:
		score_adj = i.hole3score - 2
	    elif (hdcp_adj / golfcourse.hole3handicap) >= 1:
		score_adj = i.hole3score - 1
	    elif (hdcp_adj / golfcourse.hole3handicap) <= -1:
		score_adj = i.hole3score + 1
            g_skins3.append([name,score_adj])
        if i.hole4score != 0:
	    score_adj = i.hole4score
	    if (hdcp_adj - 18) / golfcourse.hole4handicap >= 1:
		score_adj = i.hole4score - 2
	    elif (hdcp_adj / golfcourse.hole4handicap) >= 1:
		score_adj = i.hole4score - 1
	    elif (hdcp_adj / golfcourse.hole4handicap) <= -1:
		score_adj = i.hole4score + 1
            g_skins4.append([name,score_adj])
        if i.hole5score != 0:
	    score_adj = i.hole5score
	    if (hdcp_adj - 18) / golfcourse.hole5handicap >= 1:
		score_adj = i.hole5score - 2
	    elif (hdcp_adj / golfcourse.hole5handicap) >= 1:
		score_adj = i.hole5score - 1
	    elif (hdcp_adj / golfcourse.hole5handicap) <= -1:
		score_adj = i.hole5score + 1
            g_skins5.append([name,score_adj])
        if i.hole6score != 0:
	    score_adj = i.hole6score
	    if (hdcp_adj - 18) / golfcourse.hole6handicap >= 1:
		score_adj = i.hole6score - 2
	    elif (hdcp_adj / golfcourse.hole6handicap) >= 1:
		score_adj = i.hole6score - 1
	    elif (hdcp_adj / golfcourse.hole6handicap) <= -1:
		score_adj = i.hole6score + 1
            g_skins6.append([name,score_adj])
        if i.hole7score != 0:
	    score_adj = i.hole7score
	    if (hdcp_adj - 18) / golfcourse.hole7handicap >= 1:
		score_adj = i.hole7score - 2
	    elif (hdcp_adj / golfcourse.hole7handicap) >= 1:
		score_adj = i.hole7score - 1
	    elif (hdcp_adj / golfcourse.hole7handicap) <= -1:
		score_adj = i.hole7score + 1
            g_skins7.append([name,score_adj])
        if i.hole8score != 0:
	    score_adj = i.hole8score
	    if (hdcp_adj - 18) / golfcourse.hole8handicap >= 1:
		score_adj = i.hole8score - 2
	    elif (hdcp_adj / golfcourse.hole8handicap) >= 1:
		score_adj = i.hole8score - 1
	    elif (hdcp_adj / golfcourse.hole8handicap) <= -1:
		score_adj = i.hole8score + 1
            g_skins8.append([name,score_adj])
        if i.hole9score != 0:
	    score_adj = i.hole9score
	    if (hdcp_adj - 18) / golfcourse.hole9handicap >= 1:
		score_adj = i.hole9score - 2
	    elif (hdcp_adj / golfcourse.hole9handicap) >= 1:
		score_adj = i.hole9score - 1
	    elif (hdcp_adj / golfcourse.hole9handicap) <= -1:
		score_adj = i.hole9score + 1
            g_skins9.append([name,score_adj])
        if i.hole10score != 0:
	    score_adj = i.hole10score
	    if (hdcp_adj - 18) / golfcourse.hole10handicap >= 1:
		score_adj = i.hole10score - 2
	    elif (hdcp_adj / golfcourse.hole10handicap) >= 1:
		score_adj = i.hole10score - 1
	    elif (hdcp_adj / golfcourse.hole10handicap) <= -1:
		score_adj = i.hole10score + 1
            g_skins10.append([name,score_adj])
        if i.hole11score != 0:
	    score_adj = i.hole11score
	    if (hdcp_adj - 18) / golfcourse.hole11handicap >= 1:
		score_adj = i.hole11score - 2
	    elif (hdcp_adj / golfcourse.hole11handicap) >= 1:
		score_adj = i.hole11score - 1
	    elif (hdcp_adj / golfcourse.hole11handicap) <= -1:
		score_adj = i.hole11score + 1
            g_skins11.append([name,score_adj])
        if i.hole12score != 0:
	    score_adj = i.hole12score
	    if (hdcp_adj - 18) / golfcourse.hole12handicap >= 1:
		score_adj = i.hole12score - 2
	    elif (hdcp_adj / golfcourse.hole12handicap) >= 1:
		score_adj = i.hole12score - 1
	    elif (hdcp_adj / golfcourse.hole12handicap) <= -1:
		score_adj = i.hole12score + 1
            g_skins12.append([name,score_adj])
        if i.hole13score != 0:
	    score_adj = i.hole13score
	    if (hdcp_adj - 18) / golfcourse.hole13handicap >= 1:
		score_adj = i.hole13score - 2
	    elif (hdcp_adj / golfcourse.hole13handicap) >= 1:
		score_adj = i.hole13score - 1
	    elif (hdcp_adj / golfcourse.hole13handicap) <= -1:
		score_adj = i.hole13score + 1
            g_skins13.append([name,score_adj])
        if i.hole14score != 0:
	    score_adj = i.hole14score
	    if (hdcp_adj - 18) / golfcourse.hole14handicap >= 1:
		score_adj = i.hole14score - 2
	    elif (hdcp_adj / golfcourse.hole14handicap) >= 1:
		score_adj = i.hole14score - 1
	    elif (hdcp_adj / golfcourse.hole14handicap) <= -1:
		score_adj = i.hole14score + 1
            g_skins14.append([name,score_adj])
        if i.hole15score != 0:
	    score_adj = i.hole15score
	    if (hdcp_adj - 18) / golfcourse.hole15handicap >= 1:
		score_adj = i.hole15score - 2
	    elif (hdcp_adj / golfcourse.hole15handicap) >= 1:
		score_adj = i.hole15score - 1
	    elif (hdcp_adj / golfcourse.hole15handicap) <= -1:
		score_adj = i.hole15score + 1
            g_skins15.append([name,score_adj])
        if i.hole16score != 0:
	    score_adj = i.hole16score
	    if (hdcp_adj - 18) / golfcourse.hole16handicap >= 1:
		score_adj = i.hole16score - 2
	    elif (hdcp_adj / golfcourse.hole16handicap) >= 1:
		score_adj = i.hole16score - 1
	    elif (hdcp_adj / golfcourse.hole16handicap) <= -1:
		score_adj = i.hole16score + 1
            g_skins16.append([name,score_adj])
        if i.hole17score != 0:
	    score_adj = i.hole17score
	    if (hdcp_adj - 18) / golfcourse.hole17handicap >= 1:
		score_adj = i.hole17score - 2
	    elif (hdcp_adj / golfcourse.hole17handicap) >= 1:
		score_adj = i.hole17score - 1
	    elif (hdcp_adj / golfcourse.hole17handicap) <= -1:
		score_adj = i.hole17score + 1
            g_skins17.append([name,score_adj])
        if i.hole18score != 0:
	    score_adj = i.hole18score
	    if (hdcp_adj - 18) / golfcourse.hole18handicap >= 1:
		score_adj = i.hole18score - 2
	    elif (hdcp_adj / golfcourse.hole18handicap) >= 1:
		score_adj = i.hole18score - 1
	    elif (hdcp_adj / golfcourse.hole18handicap) <= -1:
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
	hdcp_adj = int(round(i.tee.teerating * i.name.handicap / i.tee.teeslope))
        score_adj = i.hole1score
        if (hdcp_adj - 18) / golfcourse.hole1handicap >= 1:
	    score_adj = i.hole1score - 2
        elif (hdcp_adj / golfcourse.hole1handicap) >= 1:
	    score_adj = i.hole1score - 1
        elif (hdcp_adj / golfcourse.hole1handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole2handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole3handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole4handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole5handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole6handicap) <= -1:
	    score_adj = i.hole6score + 1
	hole6_adj = score_adj
	if i.hole6score == 0:
	    g_hole6 = cell_start + cell_end
	    g_finished_flag = 0
	    g_front_finished_flag = 0
        elif (len(g_skins6) == 1 and str(g_skins6[0][0]) == str(i.name)) or (len(g_skins6) > 1 and g_skins6[0][1] != g_skins6[1][1] and str(g_skins6[0][0]) == str(i.name)):
            g_hole6 = cell_highlight_yellow + str(score_adj) + cell_end
        else:
            g_hole6 = cell_start + str(score_adj) + cell_end
        score_adj = i.hole7score
        if (hdcp_adj - 18) / golfcourse.hole7handicap >= 1:
	    score_adj = i.hole7score - 2
        elif (hdcp_adj / golfcourse.hole7handicap) >= 1:
	    score_adj = i.hole7score - 1
        elif (hdcp_adj / golfcourse.hole7handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole8handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole9handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole10handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole11handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole12handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole13handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole14handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole15handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole16handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole17handicap) <= -1:
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
        elif (hdcp_adj / golfcourse.hole18handicap) <= -1:
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
        hdcp_adj = int(round(i.tee.teerating * i.name.handicap / i.tee.teeslope))
        hdcp = cell_start + str(hdcp_adj) + cell_end
        net = g_total
        row = hdcp + name + tee + g_front + g_back + net
        g_arr.append([g_over_total,row])
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
        g_output += '<tr>' + '<td>' + str(rank)+ '</td>' + line[1] + '</tr>'
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
            'output_net': g_output,
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
