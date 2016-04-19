# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response


def index(response):
    content = {
        'current_page': 'Patient'
    }
    return render_to_response('templates/patient.html', content)
