from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # TODO logica da view
    return HttpResponse("Olá mundo") # transforma uma string numa resposta http
