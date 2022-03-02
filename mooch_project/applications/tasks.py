from celery import shared_task
import subprocess, sys
from scheduler.models import Order, Runtime, Jobs
# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     return x + y







        #     row.status = 'Initialized'
        #     # id_number = row.job_id
        #     # job_obj = Order.objects.filter(id=id_number)

        # row.save()

@shared_task(name="script1")
def script_test():
    args = ["powershell.exe",
        "C:\\test\\change_status.ps1"]
    p=subprocess.Popen(args,
        stdout=sys.stdout)



@shared_task(name="script2")
def change_status():
    status_obj = Runtime.objects.filter(status='Job requested')
    if status_obj:
        for row in status_obj:

            if row.status == 'Job requested':
                args = ["powershell.exe",
                "C:\\test\\script1_test.ps1"]
                p=subprocess.Popen(args,
                stdout=sys.stdout)   
    
