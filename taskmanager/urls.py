from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create', views.TaskCreate.as_view(), name='task-create'),
    url(r'update/(?P<pk>[0-9]+)', views.TaskUpdate.as_view(), name='task-update'),
    url(r'delete/(?P<pk>[0-9]+)', views.TaskDelete.as_view(), name='task-delete'),
    url(r'complete/(?P<pk>[0-9]+)', views.complete_task, name='task-complete'),
    url(r'$', views.TaskList.as_view(), name='task-list')
]
