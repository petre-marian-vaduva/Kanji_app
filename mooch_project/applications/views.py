from email.mime import application
from django.shortcuts import render
from .forms import requestipmappupgradeform, requestlorappupgradeform 
from applications.models import  lor_appversions, ipm_appversions
from django.http import HttpResponse, HttpResponseRedirect
from infrastructure.models import Instance, Server
from scheduler.models import Runtime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import admin
import subprocess, sys
from django.contrib.auth.decorators import login_required


@login_required()
def requestipmappupgradeView(request):
   form = requestipmappupgradeform()
   if request.method == "POST":
      form = requestipmappupgradeform(request.POST,empty_permitted=False)
      if form.is_valid():
         instance_name= Instance.objects.get(pk=request.POST.get('instance_name'))
         app_version= ipm_appversions.objects.values_list('app_version', flat=True).get(pk=request.POST.get('Target_version'))
         server_name = Server.objects.get(pk=request.POST.get('Server'))

         app_upgrade=Runtime(application='iPM_Application',instance_name=instance_name,application_version=app_version, server_name=server_name)
         app_upgrade.save()

         args = ["powershell.exe",
              "C:\\test\\createlog.ps1"]
         p=subprocess.Popen(args,
              stdout=sys.stdout)


         return HttpResponseRedirect('/scheduler/iPM/')
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'applications\Request_ipmappupgrade.html',{
          'form': form,
          'errors': errors,
   })				



def requestlorappupgradeView(request):
   form = requestlorappupgradeform()
   if request.method == "POST":
      form = requestlorappupgradeform(request.POST,empty_permitted=False)
      if form.is_valid():
         instance_name= Instance.objects.get(pk=request.POST.get('instance_name'))
         app_version= lor_appversions.objects.values_list('app_version', flat=True).get(pk=request.POST.get('Target_version'))
         server_name= Server.objects.get(pk=request.POST.get('Server'))

         app_upgrade=Runtime(application='LOR_Application',instance_name=instance_name,application_version=app_version, server_name=server_name)
         app_upgrade.save()
         
         args = ["powershell.exe",
              "C:\\test\\createlog.ps1"]
         p=subprocess.Popen(args,
              stdout=sys.stdout)         

         return HttpResponseRedirect('/scheduler/Lorenzo/')
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'applications\Request_lorappupgrade.html',{
          'form': form,
          'errors': errors,
   })


def all_versions(request, version):
   lor_versions = lor_appversions.objects.all()
   ipm_versions = ipm_appversions.objects.all()
   if version == 'lorenzo_version':
      return render(request, 'applications/lor_version.html', {
         'lor_versions': lor_versions
      })
   if version == 'ipm_version':
      return render(request, 'applications/ipm_version.html', {
         'ipm_versions': ipm_versions
      })


# def test(request):
#    add.delay()
#    return HttpResponse('Done')