from ipaddress import ip_address
from django.db import models

# Create your models here.
class Instance(models.Model):
    instance_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024,null=False)
    status = models.CharField(max_length=3,null=False,default='A')

    def __str__(self):
        return u'%s%s%s' %(self.instance_name, self.description, self.status)

class Server(models.Model):
    instance_name = models.ForeignKey(Instance, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=50)
    server_name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(null=False)
    description = models.CharField(max_length=1024,null=False)
    role = models.CharField(max_length=50)

    def __str__(self):
        return u'%s%s%s%s%s%s' %(self.instance_name, self.alias_name, self.server_name, self.ip_address, self.description, self.role)
