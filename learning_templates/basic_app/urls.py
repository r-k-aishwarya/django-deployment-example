from basic_app import views
from django.conf.urls import url

#TEMPLATE TAGGING

app_name = 'basic_app'

urlpatterns = [
        url(r'^other/$', views.other, name = 'other'),
        url(r'^relative/$', views.relative, name = 'relative'),
]
