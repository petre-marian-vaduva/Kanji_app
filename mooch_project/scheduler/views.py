from django.shortcuts import render
from .models import Runtime
from infrastructure.models import Instance


def instances(request, slug):
    instance = Runtime.objects.get(instance_name__instance_name=slug)
    if slug == 'Lorenzo':
        return render(request, 'scheduler/lorenzo.html', {
            'instance': instance
        })

