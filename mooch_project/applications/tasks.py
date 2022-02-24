from celery import shared_task
import subprocess, sys

# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     return x + y


@shared_task(name="script1")
def script_test():
    args = ["powershell.exe",
        "C:\\test\\change_status.ps1"]
    p=subprocess.Popen(args,
        stdout=sys.stdout)