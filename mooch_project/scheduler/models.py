from asyncio.windows_events import NULL
from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from celery import Task
from django.db import models
from datetime import datetime


class Jobs(models.Model):
    job = models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name_plural = 'Jobs'
    def __str__(self):
        return u'%s' %(self.job)


class Tasks(models.Model):
    task = models.CharField(max_length=50, null=True)
    # folder = models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name_plural = 'Tasks'
    def __str__(self):
        return u'%s' %(self.task)

class Order(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True)
    order = models.IntegerField(null=True)
    def __str__(self):
        return u'%s%s%s' %(self.job, self.task, self.order)


class Runtime(models.Model):
    instance_name = models.ForeignKey('infrastructure.Instance', on_delete=models.CASCADE)
    server_name = models.ForeignKey('infrastructure.Server', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Job requested',null=True)
    application = models.CharField(max_length=50, null=True)
    application_version = models.CharField(max_length=50, null=True)
    start_datetime = models.DateTimeField(default=datetime.now(), null=True)
    end_datetime = models.DateTimeField(default=datetime.now(), null=True)
    description = models.CharField(max_length=50, default='pending',null=True)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True)
    flag = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name_plural = 'Runtime'

    def __str__(self):
        return u'%s%s%s%s%s%s%s%s' %(self.instance_name, self.server_name, self.status, self.application, self.application_version, self.start_datetime, self.end_datetime, self.job)









