#!/usr/bin/env python3
import shutil
import psutil
#shutil stands for shell utilities

def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free_perc=du.free/du.total * 100
    return free_perc > 30

def check_cpu_health():
    cpu_usage=psutil.cpu_percent(1)
    return cpu_usage<75


if not check_disk_usage('/') and check_cpu_health:
    print("You system is in danger")
else:
    print("Everything goes right!")

