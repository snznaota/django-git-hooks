from django.conf.urls import include, url
from git_hooks import views
urlpatterns = [
    url(r'^pull/$', views.git_pull, name='git_pull'),
]
