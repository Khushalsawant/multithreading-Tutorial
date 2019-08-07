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
To initialize the settings so all threads start with the same value, 
we need to use a subclass and set the attributes in __init__()
'''

import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def show(d):
    try:
        val = d.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def f(d):
    show(d)
    d.value = random.randint(1, 100)
    show(d)

class MyLocal(threading.local):
    def __init__(self, v):
        logging.debug('Initializing %r', self)
        self.val = v

if __name__ == '__main__':
    d = MyLocal(999)
    show(d)

    for i in range(2):
        t = threading.Thread(target=f, args=(d,))
        t.start()