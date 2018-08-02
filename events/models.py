from django.db import models
from datetime import date

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
    hole1handicap = models.PositiveSmallIntegerField()
    hole2handicap = models.PositiveSmallIntegerField()
    hole3handicap = models.PositiveSmallIntegerField()
    hole4handicap = models.PositiveSmallIntegerField()
    hole5handicap = models.PositiveSmallIntegerField()
    hole6handicap = models.PositiveSmallIntegerField()
    hole7handicap = models.PositiveSmallIntegerField()
    hole8handicap = models.PositiveSmallIntegerField()
    hole9handicap = models.PositiveSmallIntegerField()
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
        return self.teename
    class Meta:
        verbose_name_plural = "Tees"

class Player(models.Model):
    name = models.CharField(max_length=40)
    handicap = models.FloatField()
    email = models.EmailField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Players"

class Leaderboard(models.Model):
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    name = models.ForeignKey(Player, on_delete=models.CASCADE)
    hole1score = models.SmallIntegerField()
    hole2score = models.SmallIntegerField()
    hole3score = models.SmallIntegerField()
    hole4score = models.SmallIntegerField()
    hole5score = models.SmallIntegerField()
    hole6score = models.SmallIntegerField()
    hole7score = models.SmallIntegerField()
    hole8score = models.SmallIntegerField()
    hole9score = models.SmallIntegerField()
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.course)
    class Meta:
        verbose_name_plural = "Leaderboards"

class Events(models.Model):
    title = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    def __str__(self):
        return str(self.title) + " " + str(self.date)
    class Meta:
        verbose_name_plural = "Events"
