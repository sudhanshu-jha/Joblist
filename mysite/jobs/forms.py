from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'job_desc','vacancy_count','job_status','publication_date' )
