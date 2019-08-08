# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 06:40:26 2019

@author: khushal
"""

'''
Condition object provides a mechanism to release lock and notify threads that are waiting on this lock.
A Condition object always associated with some kind of lock. The lock is part of condition object.

threading.Condition(lock=None)
You can pass Lock instance (or) RLock instance to this method. 
If lock argument is not given, then a new RLock object is created and used as the underlying lock.
'''

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()

'''
Example 2
implements simple producer and consumer application. producer produces the items, and consumer consumes the items produced by the producer

1. Consumer can't consume the items, if the items are not produced by producer. So consumer must wait until the producer produces items. So consumer calls the wait method of the producer object.

2. Once the consumer consumes the items, he must notify the producer, so producer produce the items.

3. Producer must wait until the consumer consumes the items.

4. Once the producer produces the items, then he must tell the consumer, Please consume the items. So he must notify the consumer.

'''

import random, time
from threading import Condition, Thread
"""
'condition' variable will be used to represent the availability of a produced
item.
"""
condition = Condition()
box = []
def producer(box, nitems):
    for i in range(nitems):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.
        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # Puts an item into box for consumption.
        condition.notify()  # Notifies the consumer about the availability.
        print("Produced:", num)
        condition.release()
def consumer(box, nitems):
    for i in range(nitems):
        condition.acquire()
        condition.wait()  # Blocks until an item is available for consumption.
        print("%s: Acquired: %s" % (time.ctime(), box.pop()))
        condition.release()
threads = []
"""
'nloops' is the number of times an item will be produced and
consumed.
"""
nloops = random.randrange(3, 6)
for func in [producer, consumer]:
    threads.append(Thread(target=func, args=(box, nloops)))
    threads[-1].start()  # Starts the thread.
for thread in threads:
    """Waits for the threads to complete before moving on
       with the main script.
    """
    thread.join()
print("All done.")
