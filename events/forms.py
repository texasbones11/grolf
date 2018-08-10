from django import forms
from models import Leaderboard

class ScorecardForm(forms.ModelForm):
    class Meta:
        model = Leaderboard
        fields = ['event', 'name', 'tee']
