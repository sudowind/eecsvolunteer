# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from eecsvolunteer.logic.utils import qset2list
from genius.models import Activity


def index(request):
    activities = Activity.objects.order_by('id')
    return render_to_response('templates/activity.html', {'activities': activities,
                                                          'current_page': 'Activity'})


def delete(request):
    data = dict()
    aid = request.GET.get('id')
    acts = Activity.objects.filter(id=aid)
    if len(acts) == 0:
        data['code'] = 0
        data['msg'] = 'Id does not exist'
    else:
        acts[0].delete()
        data['code'] = 1
    return HttpResponse(json.dumps(data), content_type='application/json')


def create(request):
    data = dict()
    if request.method == 'POST':
        place = request.POST.get('place', '')
        date = request.POST.get('date', 0)
        if place and date:
            try:
                date = int(date)
                act = Activity(date=date, place=place)
                act.save()
                data['code'] = 1    # 1表示存储成功
            except ValueError:
                data['code'] = 0
                data['msg'] = '请输入数字'
        else:
            data['code'] = 0
            data['msg'] = 'invalid place or data'
    else:
        data['code'] = 0
        data['msg'] = 'POST required'
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_activity_table(request):
    activities = Activity.objects.order_by('id')
    data = qset2list(activities)
    return HttpResponse(json.dumps(data), content_type='application/json')
