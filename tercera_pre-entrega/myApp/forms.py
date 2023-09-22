from django import forms


class PokemonForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    attack = forms.IntegerField()
    
class MasterForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    favorite_type = forms.CharField()
    
class GymForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    master = forms.CharField()
    