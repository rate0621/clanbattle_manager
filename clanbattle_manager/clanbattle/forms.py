from django import forms

from .models import Boss, AttackLog

class BossForm(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ("boss_name", 'target')


class AttackLogForm(forms.ModelForm):
    class Meta:
        model = AttackLog
        fields = ('damage',)

class BossForm(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ("boss_name", 'target')



class SearchForm(forms.Form):
    word = forms.CharField(max_length=250)
