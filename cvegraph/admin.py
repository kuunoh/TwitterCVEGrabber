from django.contrib import admin

# Register your models here.
from cvegraph.models import CVE, Time

admin.site.register(CVE)
admin.site.register(Time)
