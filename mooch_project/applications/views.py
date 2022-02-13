from django.shortcuts import render
from .forms import requestipmappupgradeform, requestlorappupgradeform 
from applications.models import  lor_appversions, ipm_appversions
from django.http import HttpResponseRedirect
from infrastructure.models import Instance
from scheduler.models import Runtime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



@permission_required('applications.view_instance')
@login_required(login_url='/login/')
def requestipmappupgradeView(request):
   form = requestipmappupgradeform()
   if request.method == "POST":
      form = requestipmappupgradeform(request.POST,empty_permitted=False)
      if form.is_valid():
         instance_name= Instance.objects.get(pk=request.POST.get('instance_name'))
         app_version= ipm_appversions.objects.values_list('app_version', flat=True).get(pk=request.POST.get('app_version'))
      
         app_upgrade=Runtime(Process='iPM_Application',instance_name=instance_name,app_version=app_version)
         app_upgrade.save()
         return HttpResponseRedirect('/Scheduler/jobs/iPM_Application/')
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'applications\Request_ipmappupgrade.html',{
          'form': form,
          'errors': errors,
   })				


@login_required(login_url='/login/')
def requestlorappupgradeView(request):
   form = requestlorappupgradeform()
   if request.method == "POST":
      form = requestlorappupgradeform(request.POST,empty_permitted=False)
      if form.is_valid():
         instance_name= Instance.objects.get(pk=request.POST.get('instance_name'))
         app_version= lor_appversions.objects.values_list('app_version', flat=True).get(pk=request.POST.get('app_version'))
					   
         app_upgrade=Runtime(Process='LOR_Application',instance_name=instance_name,app_version=app_version)
         app_upgrade.save()
         return HttpResponseRedirect('/Scheduler/jobs/LOR_Application/')
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'applications\Request_lorappupgrade.html',{
          'form': form,
          'errors': errors,
   })

