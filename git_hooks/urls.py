from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('git_hooks.views',

    url(r'^pull/$', 'git_pull', name='git_pull'),
)
