from pickle import TRUE
from django.db import models


Replication_status=(
('d', 'Draft'),
('p', 'Productionised'),
('w', 'Withdrawn')
)
# Create your models here.

class lor_appversions(models.Model):
    app_version = models.CharField(max_length=50,unique=True)
    app_version_hier = models.CharField(max_length=25,unique=True,null=True)
    status = models.CharField(max_length=3,null=False,default='A')
    description  = models.CharField(max_length=1024,null=False)
    Rep_Status = models.CharField(max_length=1, choices=Replication_status, null=TRUE)

    class Meta:
        verbose_name_plural = 'Lorenzo Application Versions'

    def __str__(self):
        if self.Rep_Status == 'p':
            return u"%s" %(self.app_version)
        if self.Rep_Status == 'd':
            return u"%s" %(self.app_version+" (draft)")
        if self.Rep_Status == 'w':
            return u"%s" %(self.app_version+" (withdrawn)")



class ipm_appversions(models.Model):
    app_version = models.CharField(max_length=50,unique=True)
    app_version_hier = models.CharField(max_length=25,unique=True,null=True)
    description  = models.CharField(max_length=1024,null=False)
    status = models.CharField(max_length=3,null=False,default='A')
    Rep_Status = models.CharField(max_length=1, choices=Replication_status, null=TRUE)

    class Meta:
        verbose_name_plural = 'iPM Application Versions'

    def __str__(self):
        if self.Rep_Status == 'p':
            return u"%s" %(self.app_version)
        if self.Rep_Status == 'd':
            return u"%s" %(self.app_version+" (draft)")
        if self.Rep_Status == 'w':
            return u"%s" %(self.app_version+" (withdrawn)")

