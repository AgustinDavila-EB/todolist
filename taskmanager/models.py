from django.db import models
from django.conf import settings

# Create your models here.


class Priority(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)


class Task(models.Model):

    def __str__(self):
        return self.name

    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    done = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    @property
    def complete(self):
        return 'Uncomplete' if self.done else 'Complete'


class Event(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=120)
    ev_id = models.CharField(max_length=40, unique=True)
    url = models.CharField(max_length=120)
    date_tz = models.CharField(max_length=64)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created = models.DateTimeField()
    changed = models.DateTimeField()
    published = models.DateTimeField()
    capacity = models.IntegerField(120)
    status = models.CharField(max_length=16)
    currency = models.CharField(max_length=10)
    online = models.BooleanField()
