from django.contrib import admin
from .models import Job

app = apps.get_app_config('mysite.jobs')
for model_name, model in app.models.items():
    admin.site.register(model)

