from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from cvegraph.models import CVE, Time


# Create your views here.
def index(request):
    context = {
        "home_page": "active"
    }
    return render(request, 'index.html', context=context)


def day(request):
    context = {"day_page": "active"}
    return render(request, 'day.html', context)


def week(request):
    context = {"week_page": "active"}
    return render(request, 'week.html', context)


def about(request):
    context = {"about_page": "active"}
    return render(request, 'about.html', context)


def cve_chart_today(request):

    time = Time.objects.filter(id=1).values_list('last_retrieve_time').get()

    return JsonResponse(list(CVE.objects.all().filter(today_occurrence_number__gt=0).order_by('-today_occurrence_number')
                             .values()), safe=False)


def cve_chart_weekly(request):

    return JsonResponse(list(CVE.objects.all().filter(weekly_occurrence_number__gt=0)
                             .order_by('-weekly_occurrence_number')
                             .values()), safe=False)


def get_time(request):
    time = Time.objects.filter(id=1).values_list('last_retrieve_time').get()
    return JsonResponse(list(time), safe=False)
