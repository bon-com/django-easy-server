from django.contrib import admin
from django.urls import path
from .views import index, index_json, index_html

urlpatterns = [
    path("admin/", admin.site.urls),
    path("simple/", index),
    path("simple/json/", index_json),
    path("simple/html/", index_html),
]
