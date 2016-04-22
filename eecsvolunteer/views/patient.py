# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from genius.models import CaseHistory, Activity, CaseHistoryStatus


def index(request):
    if 'id' in request.session:
        cid = request.session['id']
        case = CaseHistory.objects.filter(id=cid).values().first()
        activity = Activity.objects.order_by('-id')[0]
        wait_count = CaseHistory.objects.filter(activity=activity, status=CaseHistoryStatus.waiting_for_repair).count()
        case['wait_count'] = wait_count
        content = {
            'current_page': 'Patient',
            'case': case
        }
        return render_to_response('templates/patient/patient_submit.html', content)
    else:
        content = {
            'current_page': 'Patient'
        }
        return render_to_response('templates/patient/patient.html', content)


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
        data['code'] = 1
        request.session['id'] = data['id']
    else:
        data['code'] = 0
        data['msg'] = 'POST required'
    return HttpResponse(json.dumps(data), content_type='application/json')
