from django.conf.urls import include, url

urlpatterns = ['git_hooks.views',

    url(r'^pull/$', 'git_pull', name='git_pull'),
]
