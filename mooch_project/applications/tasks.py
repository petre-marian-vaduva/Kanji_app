from celery import shared_task
import subprocess, sys
from scheduler.models import Order, Runtime, Jobs, Tasks
import subprocess, sys
import time
# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     return x + y





@shared_task(name="script1")
def script_test():
    args = ["powershell.exe", "C:\\test\\change_status.ps1"]
    p=subprocess.Popen(args,
        stdout=sys.stdout)



@shared_task(name="script2")
def change_status():
    status_obj = Runtime.objects.filter(status='test')
    if status_obj:
        for row in status_obj:     
            row.status = 'Initialized'
            id_number = row.job_id
            job_obj = Order.objects.filter(job_id=id_number)
            task_name = job_obj[0].task
            task_order = job_obj[0].order 
            row.order = task_order
            current_job = row.job.job
            row.save()
            begin_script_path = 'C:\\test\\'
            folder = current_job
            script_path = begin_script_path + folder + '\\' + task_name
            time.sleep(5)
            args = ["powershell.exe", script_path]
            p=subprocess.Popen(args, stdout=sys.stdout)
            

            # if row.status == 'Job requested':
            #     args = ["powershell.exe",
            #     "C:\\test\\script1_test.ps1"]
            #     p=subprocess.Popen(args,
            #     stdout=sys.stdout)   
    
