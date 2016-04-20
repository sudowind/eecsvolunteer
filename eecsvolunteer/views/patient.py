# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from genius.models import CaseHistory, Activity, CaseHistoryStatus


def index(request):
    content = {
        'current_page': 'Patient'
    }
    return render_to_response('templates/patient.html', content)


@csrf_exempt
def add_case(request):
    data = dict()
    activity = Activity.objects.order_by('-id')[0]
    if request.method == 'POST':
        owner = request.POST.get('owner', '')
        contact = request.POST.get('contact', '')
        model = request.POST.get('model', '')
        problem = request.POST.get('problem', '')
        case = CaseHistory(owner=owner, contact=contact, computer_model=model, problem=problem, activity=activity)
        case.save()
        data['id'] = getattr(case, 'id')
        data['code'] = 1
    else:
        data['code'] = 0
        data['msg'] = 'POST required'
    wait_count = CaseHistory.objects.filter(activity=activity, status=CaseHistoryStatus.waiting_for_repair).count()
    data['wait_count'] = wait_count - 1
    return HttpResponse(json.dumps(data), content_type='application/json')
