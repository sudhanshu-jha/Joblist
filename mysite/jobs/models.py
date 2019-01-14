from __future__ import unicode_literals

from django.db import models


class Job(models.Model):
    NEW = 1
    OPEN = 2
    CLOSE = 3
    JOB_STATUS = ((NEW, "New"), (OPEN, "Open"), (CLOSE, "Close"))
    title = models.CharField(max_length=50)
    job_desc = models.TextField()
    vacancy_count = models.IntegerField(default=0)
    job_status = models.PositiveSmallIntegerField(
        choices=JOB_STATUS, blank=True, null=True
    )
    publication_date = models.DateField(blank=True, null=True)
