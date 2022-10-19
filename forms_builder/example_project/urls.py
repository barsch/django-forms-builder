from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from forms_builder.forms import urls as form_urls
from forms_builder.forms.models import Form


admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("forms/", include(form_urls)),
    path(
        "",
        lambda request: render(request, "index.html", {"forms": Form.objects.all()}),
    ),
]
