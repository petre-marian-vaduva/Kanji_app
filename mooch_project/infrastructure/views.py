from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from infrastructure.models import Instance,Server


def ajax_admin_getall_machines_for_instance(request, instance_name):
    callback = request.GET.get('callback', '')
    instance_ID=Instance.objects.filter(instance_name__exact=instance_name)
    instance = get_object_or_404(Instance, pk=instance_ID[0].id)
    machines = Server.objects.filter(instance_name=instance_ID[0].id)
    qs=[ {"id":Server.id,"name":Server.server_name} for Server in machines ]
    return JsonResponse(qs,safe=False)
