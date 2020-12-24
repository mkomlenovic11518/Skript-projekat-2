from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Zdravo')


def fProizvodjac(request):
    return render(request,'baza/formProizvodjac.html')