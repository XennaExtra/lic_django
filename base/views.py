from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Examination, Outpost

def index(request):
    return render(request, 'base/homepage.html')
def badania(request):
    exams = Examination.objects.all().order_by('category').values
    return render(request, 'base/lista_badan.html', {'exams': exams})
def placowki(request):
    places = Outpost.objects.all().order_by('city').values
    return render(request, 'base/nasze_placowki.html', {'places': places})
