# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:26:32 2019

@author: KS5046082
"""


'''
Thread-local data is data whose values are thread specific.
To manage thread-local data, just create an instance of local (or a subclass) and
store attributes on it
'''
#https://docs.python.org/3/library/threading.html

import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s) %(message)s',)

def show(d):
    try:
        val = d.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def f(d):
    show(d)
    d.val = random.randint(1, 100)
    show(d)

if __name__ == '__main__':
    #threading.local()
    d = threading.local()
    show(d)
    d.val = 999 #To manage thread-local data, just create an instance of local
    show(d)
    
    for i in range(2):
        t = threading.Thread(target=f, args=(d,))
        t.start()




'''
Example of threading.local()
Thread Local Storage is a means where variables declared as thread local are made specific to thread instances.
e.g. Use thread-local variables
'''

import threading

thread_local = threading.local()

def f(n):
    print( get_local_x())
    set_local_x(n)
    print( get_local_x())

def get_local_x():
    try:
        return thread_local.x
    except AttributeError as e:
        return "Local x not yet set"

def set_local_x(n):
    thread_local.x = n

thread1 = threading.Thread(target=f, args=(1,),name='thread1')
thread2 = threading.Thread(target=f, args=(2,),name='thread2')
thread1.start()
thread2.start()

'''
Anther example f threading local
'''

# Thread Local Storage: Example Python Program

 

import threading

userName = threading.local() 

def SessionThread(userName_in):

    userName.val = userName_in

    print(userName.val)      

Session1 = threading.Thread(target=SessionThread,args=('User1',))

Session2 = threading.Thread(target=SessionThread,args=('User2',))

# start the session threads

Session1.start()

Session2.start() 

# wait till the session threads are complete

Session1.join()

Session2.join()