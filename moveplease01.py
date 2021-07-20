#!/usr/bin/env python3

# import libraries
import shutil
import os

# makr start position for script
os.chdir('/home/student/mycode/')

#move file/folder to selected location
shutil.move('raynor.obj', 'ceph_storage/')

#naming prompt to not overwrite a file with a move method
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

