# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:49:19 2019

@author: khushal
"""

'''
Thread synchronization ensures that two or more concurrent threads,
do not simultaneously execute some particular program segment i.e.
parts of the program where the shared resource is accessed.

In Below example, Each thread has a target function thread_task
in which increment function is called 500000 times.
Here, the shared resource is "increment()" function which in icrementing the value of global var. x


Concurrent accesses to shared resource can lead to race condition.
Race Condition =
A race condition occurs when two or more threads can access shared data and
they try to change it at the same time. As a result, the values of variables may be unpredictable
and vary depending on the timings of context switches of the processes.

'''


import threading 

# global variable x 
x = 0

def increment(): 
	global x 
	x += 1

def thread_task():
    print("\n Task has been assigned to thread: {}".format(threading.current_thread().name))
    for _ in range(500000): 
        increment() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = threading.Thread(target=thread_task,name ='t1') 
	t2 = threading.Thread(target=thread_task,name='t2') 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__":
    print("Program is showing an example of Race Condition")
    for i in range(10):
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 



#### Explanation for Thread Synchronization And Solution fr Race conditions.
'''
threading module provides a Lock class to deal with the race conditions. 

Lock class provides following methods:

acquire([blocking]) : To acquire a lock. A lock can be blocking or non-blocking.
When invoked with the blocking argument set to True (the default), thread execution is blocked until the lock is unlocked, then lock is set to locked and return True.
When invoked with the blocking argument set to False, thread execution is not blocked. If lock is unlocked, then set it to locked and return True else return False immediately.
release() : To release a lock.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
If lock is already unlocked, a ThreadError is raised.
'''

import threading 

# global variable x 
x = 0

def increment_1(): 
	global x 
	x += 1

def thread_task_1(lock):
    print("\n Task has been assigned to thread: {}".format(threading.current_thread().name))
    '''
    we apply lock using lock.acquire() method. As soon as a lock is acquired, no other thread can access the critical section (here, increment function) until the lock is released using lock.release() method.
    '''
    for _ in range(500000): 
        lock.acquire()
        increment_1()
        lock.release()

def main_task():
    global x
    x = 0 # setting global variable x as 0
    lock = threading.Lock() # creating a Lock , Firstly, a Lock object is created using:
    # creating threads  & Then, lock is passed as target function argument:
    t1 = threading.Thread(target=thread_task_1,args=(lock,),name ='t01') 
    t2 = threading.Thread(target=thread_task_1,args=(lock,),name='t02')
    # start threads 
    t1.start()
    t2.start()
    # wait until threads finish their job
    t1.join()
    t2.join() 

if __name__ == "__main__":
    print("Program is showing an example of Thread Synchronization")
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x)) 

