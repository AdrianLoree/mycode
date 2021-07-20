#!/usr/bin/python3

#parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0
#open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    #loop over the file
    for line in kfile:
        #if the pattern  that appears for a failed login
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as logfail = logfail +1
            print(line.split(" ")[-1])#the following elif agumention MUST be AFTER we check for a fail
        #this statement assumes the if statement above it tested false
        elif "-] Authorization failed" in line:
            successful += 1

print("The number of failed log in attempts is", loginfail)

print('The number of successful log in attempts is', successful)
