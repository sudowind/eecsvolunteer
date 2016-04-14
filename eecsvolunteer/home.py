# coding=utf-8
from django.shortcuts import render_to_response


def hello(request):
    content = dict(
        current_page='homepage'
    )
    return render_to_response('home.html', content)

