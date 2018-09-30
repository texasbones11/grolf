from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class GolfCourse(models.Model):
    course = models.CharField(max_length=40)
    hole1par = models.PositiveSmallIntegerField()
    hole2par = models.PositiveSmallIntegerField()
    hole3par = models.PositiveSmallIntegerField()
    hole4par = models.PositiveSmallIntegerField()
    hole5par = models.PositiveSmallIntegerField()
    hole6par = models.PositiveSmallIntegerField()
    hole7par = models.PositiveSmallIntegerField()
    hole8par = models.PositiveSmallIntegerField()
    hole9par = models.PositiveSmallIntegerField()
    hole10par = models.PositiveSmallIntegerField()
    hole11par = models.PositiveSmallIntegerField()
    hole12par = models.PositiveSmallIntegerField()
    hole13par = models.PositiveSmallIntegerField()
    hole14par = models.PositiveSmallIntegerField()
    hole15par = models.PositiveSmallIntegerField()
    hole16par = models.PositiveSmallIntegerField()
    hole17par = models.PositiveSmallIntegerField()
    hole18par = models.PositiveSmallIntegerField()
    hole1handicap = models.PositiveSmallIntegerField()
    hole2handicap = models.PositiveSmallIntegerField()
    hole3handicap = models.PositiveSmallIntegerField()
    hole4handicap = models.PositiveSmallIntegerField()
    hole5handicap = models.PositiveSmallIntegerField()
    hole6handicap = models.PositiveSmallIntegerField()
    hole7handicap = models.PositiveSmallIntegerField()
    hole8handicap = models.PositiveSmallIntegerField()
    hole9handicap = models.PositiveSmallIntegerField()
    hole10handicap = models.PositiveSmallIntegerField()
    hole11handicap = models.PositiveSmallIntegerField()
    hole12handicap = models.PositiveSmallIntegerField()
    hole13handicap = models.PositiveSmallIntegerField()
    hole14handicap = models.PositiveSmallIntegerField()
    hole15handicap = models.PositiveSmallIntegerField()
    hole16handicap = models.PositiveSmallIntegerField()
    hole17handicap = models.PositiveSmallIntegerField()
    hole18handicap = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.course
    class Meta:
        verbose_name_plural = "Golf Courses"

class Tee(models.Model):
    teename = models.CharField(max_length=40)
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    teeslope = models.FloatField()
    teerating = models.FloatField()
    teecolor = models.CharField(max_length=10)
    def __str__(self):
        return str(self.teename) + " " + str(self.course)
    class Meta:
        verbose_name_plural = "Tees"

class Handicap(models.Model):
    name = models.ForeignKey(User, unique=True)
    handicap = models.FloatField()
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.name.username + " - " + str(self.date)
    class Meta:
        verbose_name_plural = "Handicap"

class Events(models.Model):
    tag = models.CharField(max_length=40, default="")
    title = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    teamscoring = models.BooleanField(default=False)
    netteamscoring = models.BooleanField(default=False)
    netscoring = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default="")
    def __str__(self):
        return str(self.tag) + " - " + str(self.title) + " - " + str(self.date)
    class Meta:
        verbose_name_plural = "Events"

class Leaderboard(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.ForeignKey(Handicap)
    hole1score = models.SmallIntegerField(blank=True,default=0)
    hole2score = models.SmallIntegerField(blank=True,default=0)
    hole3score = models.SmallIntegerField(blank=True,default=0)
    hole4score = models.SmallIntegerField(blank=True,default=0)
    hole5score = models.SmallIntegerField(blank=True,default=0)
    hole6score = models.SmallIntegerField(blank=True,default=0)
    hole7score = models.SmallIntegerField(blank=True,default=0)
    hole8score = models.SmallIntegerField(blank=True,default=0)
    hole9score = models.SmallIntegerField(blank=True,default=0)
    hole10score = models.SmallIntegerField(blank=True,default=0)
    hole11score = models.SmallIntegerField(blank=True,default=0)
    hole12score = models.SmallIntegerField(blank=True,default=0)
    hole13score = models.SmallIntegerField(blank=True,default=0)
    hole14score = models.SmallIntegerField(blank=True,default=0)
    hole15score = models.SmallIntegerField(blank=True,default=0)
    hole16score = models.SmallIntegerField(blank=True,default=0)
    hole17score = models.SmallIntegerField(blank=True,default=0)
    hole18score = models.SmallIntegerField(blank=True,default=0)
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    skinsgross = models.BooleanField(default=True)
    skinsnet = models.BooleanField(default=False)
    gross = models.BooleanField(default=False)
    net = models.BooleanField(default=True)
    eagles = models.BooleanField(default=False)
    def __str__(self):
        return str(self.event) + " - " + str(self.name)
    class Meta:
        verbose_name_plural = "Leaderboards"

class TeamLeaderboard(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=40)
    player1 = models.ForeignKey(Leaderboard, on_delete=models.CASCADE, related_name='first_player')
    player2 = models.ForeignKey(Leaderboard, on_delete=models.CASCADE, related_name='second_player')
    def __str__(self):
        return str(self.event) + " - " + str(self.teamname)
    class Meta:
        verbose_name_plural = "TeamLeaderboards"
