from django.shortcuts import render
from .models import Runtime
from infrastructure.models import Instance



def home(request):
    all_instances = Runtime.objects.all()
    return render(request, 'scheduler/home.html')

# def instances(request, slug):
#     instance_lorenzo = Runtime.objects.filter(instance_name__instance_name='Lorenzo')
#     instance_ipm = Runtime.objects.filter(instance_name__instance_name='iPM')
#     if slug == 'Lorenzo':
#         return render(request, 'scheduler/lorenzo.html', {
#             'instance_lorenzo': instance_lorenzo
#         })
#     elif slug == 'iPM':
#         return render(request, 'scheduler/ipm.html', {
#             'instance_ipm': instance_ipm
#         })

