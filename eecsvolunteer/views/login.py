# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    content = {
        'current_page': 'login',
    }
    return render_to_response('templates/login.html', content)


def login(request):
    pass


def registered(request):
    pass


def logout(request):
    pass
