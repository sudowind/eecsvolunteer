import json
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from genius.models import ActivityForm, Activity


def index(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/activity/')

    else:
        form = ActivityForm()
    activities = Activity.objects.order_by('id')

    return render_to_response('templates/activity.html', {'activities': activities, 'form': form},
                              context_instance=RequestContext(request))


def delete(request):
    data = {}
    aid = request.GET.get('id')
    acts = Activity.objects.filter(id=aid)
    if len(acts) == 0:
        data['code'] = 0
        data['msg'] = 'Id does not exist'
    else:
        acts[0].delete()
        data['code'] = 1
    return HttpResponse(json.dumps(data), content_type='application/json')
