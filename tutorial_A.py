# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:33:26 2019

@author: khushal
"""

# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import os

def print_cube(num): 
    print("\n Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print(" Cube: {}".format(num * num * num)) 

def print_square(num): 
    print("\n Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print(" Square: {}".format(num * num)) 

if __name__ == "__main__":
    '''
    use os.getpid() function to get ID of current process.
    And the process ID remains same for all threads.
    '''
	# print ID of current process
    print("ID of process running main program: {}".format(os.getpid())) 

	# print name of main thread 
    print("Main thread name: {}".format(threading.main_thread().name)) 
    
	# creating thread 
    '''
    while creating a thread, create an object of Thread class. It takes following args,
    1. target: the function to be executed by thread
    2. args: the arguments to be passed to the target function
    3. name : Define a name to a Thread
    '''
    t1 = threading.Thread(target=print_square, args=(10,),name='Square') 
    t2 = threading.Thread(target=print_cube, args=(10,),name='Cube') 

	# starting thread 1 
    '''
    To start a thread, we use start method of Thread class.
    '''
    t1.start() 
	# starting thread 2 
    t2.start() 

	# wait until thread 1 is completely executed 
    t1.join() 
	# wait until thread 2 is completely executed 
    t2.join() 

	# both threads completely executed 
    print("Done!") 