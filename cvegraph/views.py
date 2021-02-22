from django.shortcuts import render
from django.http import JsonResponse
from cvegraph.models import CVE


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
    labels = []
    data = []

    # queryset = CVE.objects.values('cve_id', 'today_occurrence_number').filter(today_occurrence_number__gt=1)
    queryset = CVE.objects.all().filter(today_occurrence_number__gt=0).order_by('-today_occurrence_number')[:10]
    for entry in queryset:
        labels.append(entry.cve_id)
        data.append(entry.today_occurrence_number)

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })


def cve_chart_weekly(request):
    labels = []
    data = []

    # queryset = CVE.objects.values('cve_id', 'today_occurrence_number').filter(today_occurrence_number__gt=1)
    queryset = CVE.objects.all().filter(weekly_occurrence_number__gt=0).order_by('-weekly_occurrence_number')[:10]
    for entry in queryset:
        labels.append(entry.cve_id)
        data.append(entry.weekly_occurrence_number)

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })
