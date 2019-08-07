# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:18:25 2019

@author: khushal
"""

'''
A semaphore manages an internal counter which is decremented by each acquire() call
and incremented by each release() call.
The counter can never go below zero;
when acquire() finds that it is zero, it blocks,
waiting until some other thread calls release().

For example, we may want to use semaphore in a situation where we need to support concurrent connections/downloads. Semaphores are also often used to guard resources with limited capacity, for example, a database server.

'''

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def f(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.5)
        pool.makeInactive(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = threading.Semaphore(3) # Number tells us max number of threads run concurrently
    for i in range(10):
        t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
        t.start()
