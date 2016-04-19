# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response

from genius.models import CaseHistory


def index(request):
    content = {
        'current_page': 'Maintain'
    }
    return render_to_response('templates/maintain.html', content)


def apply(request):
    data = dict()
    cid = request.GET.get('id')
    cases = CaseHistory.objects.filter(id=cid)
    if len(cases) == 0:
        data['code'] = 0
        data['msg'] = 'Id does not exist'
    else:
        if cases[0].status == 2:
            data['code'] = 2
            data['msg'] = '该病例不处于可维修状态'
        else:
            cases[0].status = 2
            cases[0].save()
            data['code'] = 1
    return HttpResponse(json.dumps(data), content_type='application/json')


def diagnose(request):
    data = dict()
    if request.method == 'POST':
        cid = request.POST.get('id')
        solution = request.POST.get('solution', '')
        volunteer = request.POST.get('volunteer', '')
        if solution and volunteer:
            cases = CaseHistory.objects.filter(id=cid)
            if len(cases) == 0:
                data['code'] = 0
                data['msg'] = 'Id does not exist'
            else:
                cases[0].solution = solution
                cases[0].volunteer = volunteer
                cases[0].save()
                data['code'] = 1
        else:
            data['code'] = 0
            data['msg'] = 'invalid solution or volunteer'
    else:
        data['code'] = 0
        data['msg'] = 'POST required'
    return HttpResponse(json.dumps(data), content_type='application/json')