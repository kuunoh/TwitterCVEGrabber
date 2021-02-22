from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('day/', views.day, name='day'),
    path('week/', views.week, name='week'),
    path('about/', views.about, name='about'),
    path('today_chart/', views.cve_chart_today, name='cve_chart_today'),
    path('weekly_chart/', views.cve_chart_weekly, name='cve_chart_weekly')
]
