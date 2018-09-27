from django import forms
from models import Leaderboard

class ScorecardForm(forms.ModelForm):
    class Meta:
        model = Leaderboard
        fields = ['name','tee']
        widgets = {'event': forms.HiddenInput(), 'id': forms.HiddenInput()}
    def __init__(self, *args, **kwargs):
        supoer(ScorecardForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True
