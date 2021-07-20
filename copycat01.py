#!/usr/bin/env python3
'''lab 16 copying files and folders'''

# import the shutil library
import shutil

# import the os library
import os

# place for the python program to start from
os.chdir("/home/student/mycode/")

# copy file to file b
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# The following line will create the directory if it does not exist already
#copy folder to folder b
shutil.copytree("5g_research/", "5g_research_backup/")



