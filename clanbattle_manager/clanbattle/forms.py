from django import forms

from .models import Boss

class BossForm(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ("boss_name", 'target')


class SearchForm(forms.Form):
    word = forms.CharField(max_length=250)
