from django.db import models

# Create your models here.


class CVE(models.Model):
    """ This object represents a CVE """
    cve_id = models.CharField(primary_key=True, max_length=255, help_text='Unique ID for this particular CVE')
    today_occurrence_number = models.IntegerField(null=True, default=None, blank=True)
    weekly_occurrence_number = models.IntegerField(null=True, default=None)
    link = models.CharField(max_length=255, help_text='Link for getting further information on this particular CVE')

    def __str__(self):
        return self.cve_id


class Time(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    last_retrieve_time = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.last_retrieve_time)
