from django import forms
from .models import Noticia, Area

class NotForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('titulo', 'texto','area','foto')


class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = ('descricao', 'cor', 'status')
		