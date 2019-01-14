from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.jobs import views


from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", TemplateView.as_view(template_name="home.html"), name="home"),
    url(r"^jobs/$", views.job_list, name="job_list"),
    url(r"^jobs/create/$", views.job_create, name="job_create"),
    url(r"^jobs/(?P<pk>\d+)/update/$", views.job_update, name="job_update"),
    url(r"^jobs/(?P<pk>\d+)/delete/$", views.job_delete, name="job_delete"),
]
