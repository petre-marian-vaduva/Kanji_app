from django.db import models

# Create your models here.

class lor_appversions(models.Model):
    app_version = models.CharField(max_length=50,unique=True)
    app_version_hier = models.CharField(max_length=25,unique=True,null=True)
    status = models.CharField(max_length=3,null=False,default='A')
    description  = models.CharField(max_length=1024,null=False)

    class Meta:
        verbose_name_plural = 'Lorenzo Application Versions'

    def __str__(self):
        return u"%s" %(self.app_version)




class ipm_appversions(models.Model):
    app_version = models.CharField(max_length=50,unique=True)
    app_version_hier = models.CharField(max_length=25,unique=True,null=True)
    description  = models.CharField(max_length=1024,null=False)
    status = models.CharField(max_length=3,null=False,default='A')

    class Meta:
        verbose_name_plural = 'iPM Application Versions'

    def __str__(self):
        return u'%s' %(self.app_version)

