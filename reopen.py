#!/usr/bin/env python
import psutil
import subprocess
from datetime import datetime
import threading

from tempita import sub


class application_reopen:
    def __init__(self, application_name):
        self.application = str(application_name)
        self.current_time = datetime.now()
        self.reopen_lock = threading.Lock()
    
    # reopen a process that was closed
    def reopen(self):
        self.application_status = self.check_if_the_process_is_running(self.application)
         # Check if any Discord process was running or not.
        while (self.application_run):
            with self.reopen_lock:
                if self.application_status == True:
                    print(self.application, 'is already running at:', self.current_time)
                else:
                    print('-------------------------------------------')
                    print(self.application, 'is not running at: ', self.current_time)
                    print('Opening ', self.application)
                    subprocess.call([self.application])
    
    def loop(self):
        print('Reopen process of',self.application,'started')
        self.application_run = True
        thread = threading.Thread(target=self.reopen, daemon=True)
        thread.start()
    
    def endloop(self):
        print('Reopen process of',self.application,'stopped')
        self.application_run = False
        #subprocess.call(['kill', self.application]) # kills the process also
        subprocess.call(['wait'])


    # check if the process is running
    def check_if_the_process_is_running(self, processName):
        #Check if there is any running process that contains the given name processName.
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;



