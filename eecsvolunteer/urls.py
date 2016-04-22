"""eecsvolunteer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from eecsvolunteer.views import home, activity, patient, maintain, case_history

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),

    url(r'^home/$', home.login),
    url(r'^activity/$', activity.index),
    url(r'^activity/delete/', activity.delete),
    url(r'^activity/create/', activity.create),
    url(r'^activity/get_activity_table/', activity.get_activity_table),

    url(r'^patient/$', patient.index),
    url(r'^patient/add_case/', patient.add_case),

    url(r'^maintain/$', maintain.index),
    url(r'^maintain/apply/', maintain.apply),
    url(r'^maintain/success/', maintain.success),
    url(r'^maintain/fail/', maintain.fail),

    url(r'^case_history/get_case_table/', case_history.get_case_table),
]
