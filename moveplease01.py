#!/usr/bin/env python3
'''A simple script to move two files into another folder'''

# import standard libraries
import shutil
import os

def main():
    '''called at runtime'''
    #mark start position for script
    os.chdir('/home/student/mycode/')
    
    #move file/folder to selected location
    shutil.move('raynor.obj', 'ceph_storage/')
    
    #naming prompt to not overwrite a file with a move method
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
