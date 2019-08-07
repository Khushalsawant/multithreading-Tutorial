# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:41:36 2019

@author: khushal
"""

'''
daemon threads = 
Daemons are only useful when the main program is running,
and it's okay to kill them off once the other non-daemon threads have exited.
Without daemon threads, we have to keep track of them, and tell them to exit,
before our program can completely quit.
By setting them as daemon threads, we can let them run and forget about them,
and when our program quits, any daemon threads are killed automatically.

To designate a thread as a daemon, we call its setDaemon() method with a boolean argument.
The default setting for a thread is non-daemon.
So, passing True turns the daemon mode on.
'''

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
    '''
    it does not have "Exiting" message from the daemon thread,
    since all of the non-daemon threads (including the main thread) exit before the daemon thread wakes up from its five second sleep.
    '''
    time.sleep(5) # To verify the above comment Kindly make this line inaactive & run the program.
    logging.debug('Exiting')

if __name__ == '__main__':

	t = threading.Thread(name='non-daemon', target=n)

	d = threading.Thread(name='daemon', target=d)
	d.setDaemon(True)

	d.start()
	t.start()

'''
To wait until a daemon thread has completed its work
we may want to use join() method.

Also pass a timeout argument which is a float representing the number of seconds to wait for the thread to become inactive.
If the thread does not complete within the timeout period, join() returns anyway.
As join() always returns None, we must call isAlive() after join() to decide whether a timeout happened,
If the thread is still alive, the join() call timed out.
'''
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

    t = threading.Thread(name='non-daemon', target=n)
    d = threading.Thread(name='daemon', target=d)
    d.setDaemon(True)

    d.start()
    t.start()

    d.join(3.0)
    print('Check whether Thread=d is live after delay of 3secs d.isAlive()', d.isAlive())
    t.join()
    print('Thread-d will be dead after 3sec d.isAlive()', d.isAlive())
