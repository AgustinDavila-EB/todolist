from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .models import Task, Event
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from eventbrite import Eventbrite


class Login(LoginView):
    pass


class Logout(LogoutView):
    template_name = ''


class TaskList(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')


class EventList(LoginRequiredMixin, TemplateView):
    template_name = "event_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.get_event()
        return context

    def get_event(self):
        social = self.request.user.social_auth.filter(provider='eventbrite')[0]
        eb = Eventbrite(social.access_token)
        events = eb.get('/users/me/events/')
        return events


def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return redirect('task-list')
