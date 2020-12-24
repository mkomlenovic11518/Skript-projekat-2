from django.forms import ModelForm
from .models import Proizvodjac,Roba

class ProizvodjacForm(ModelForm):
    class Meta:
        model=Proizvodjac
        fields=('naziv_proizvodjac','sifra_proizvodjac','owner')


class RobaForm(ModelForm):
    class Meta:
        model=Roba
        fields=('naziv_robe','sifra_robe','kolicina','proizvodjac','owner')