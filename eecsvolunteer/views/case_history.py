# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from eecsvolunteer.logic.utils import qset2list
from genius.models import CaseHistory


def get_case_table(request):
    aid = request.GET.get('aid')
    cases = CaseHistory.objects.filter(activity=aid).order_by('id')
    data = qset2list(cases)
    return HttpResponse(json.dumps(data), content_type='application/json')
