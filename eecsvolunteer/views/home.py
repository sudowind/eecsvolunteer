# coding=utf-8
from django.shortcuts import render_to_response


def hello(request):
    content = dict(
        current_page='Home'
    )
    return render_to_response('templates/home.html', content)

