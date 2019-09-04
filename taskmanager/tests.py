from django.test import TestCase, Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import transaction
from .models import Priority, Task


class test_models(TestCase):

    def setUp(self):
        self.p1 = Priority.objects.create(name='low')
        self.p2 = Priority.objects.create(name='normal')
        self.p3 = Priority.objects.create(name='urgent')
        self.user1 = User.objects.create_user('foo', password='bar')
        self.user1.is_superuser = True
        self.user1.is_staff = True
        self.t1 = {
            'name': 'task1',
            'author': self.user1,
            'priority': self.p1
        }

    def test_priority(self):
        prio = Priority.objects.all()
        self.assertEqual(3, len(prio))

    def test_priority_name(self):
        self.assertEqual('low', self.p1.name)
        self.assertEqual('normal', self.p2.name)
        self.assertEqual('urgent', self.p3.name)

    def test_user(self):
        self.assertEqual('foo', self.user1.username)

    def test_fail_create_task(self):
        try:
            with transaction.atomic():
                task1 = Task.objects.create()
        except Exception:
            pass

    def test_create_task(self):
        task1 = Task.objects.create(**self.t1)
        self.assertEqual(task1.name, 'task1')

    def events_create(self):
        pass


class test_view(TestCase):
    def setUp(self):
        pass

    def test_para_travis(self):
        pass
