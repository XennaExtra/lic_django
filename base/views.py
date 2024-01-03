from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'base/homepage.html')

