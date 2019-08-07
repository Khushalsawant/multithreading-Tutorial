# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:28:10 2019

@author: khushal
"""

'''
Without logging module
To get the Thread Name i.e. which thread is currently running.
'''
import threading
import time

def f1():
    print("\n",threading.currentThread().getName(), 'Starting')
    time.sleep(1)
    print("\n",threading.currentThread().getName(), 'Exiting')

def f2():
    print("\n",threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print("\n",threading.currentThread().getName(), 'Exiting')

def f3():
    print("\n",threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print("\n",threading.currentThread().getName(), 'Exiting')

t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

'''
With logging module
To get the Thread Name i.e. which thread is currently running.
logging module which will embed the thread name in every log message using the formatter code %(threadName)
'''
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                      format='[%(levelname)s] (%(threadName)-9s) %(message)s',)

def f1():
    logging.debug('Starting')
    time.sleep(1)
    logging.debug('Exiting')

def f2():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def f3():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()