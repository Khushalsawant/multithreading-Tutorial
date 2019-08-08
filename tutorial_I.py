# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 08:21:15 2019

@author: khushal
"""

import threading

sema = threading.Semaphore()
def count():
    sema.acquire()
    print("\n Task has been assigned to thread: {}".format(threading.current_thread().name))
    print("\n Start")
    for i in range(1, 4):
        print(i)
    sema.release()
    
thread1 = threading.Thread(target=count,name='thread1')
thread2 = threading.Thread(target=count,name='thread2')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("done")