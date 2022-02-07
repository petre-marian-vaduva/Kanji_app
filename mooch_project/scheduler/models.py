from email.policy import default
from django.db import models
from datetime import datetime

class Runtime(models.Model):
    instance_name = models.ForeignKey('infrastructure.Instance', on_delete=models.CASCADE)
    server_name = models.ForeignKey('infrastructure.Server', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Job requested')
    application = models.CharField(max_length=50)
    application_version = models.CharField(max_length=50)
    start_datetime = models.DateTimeField(default=datetime.now())
    end_datetime = models.DateTimeField()
    description = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return u'%s%s%s%s%s%s%s%s' %(self.instance_name, self.server_name, self.status, self.application, self.application_version, self.start_datetime, self.end_datetime, self.description)
