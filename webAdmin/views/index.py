import json

import requests
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'rentPc/index/index.html')
