#!/usr/bin/env python3
#mydir = {}
#mylist = [mydir]
mylist =[]
username = input("Name :")
userage = input("age :")
userheight = input("height :")

#mydir.update(username.split("Name : ", username))
#mydir.update(userage.split("Age : ", userage))
#mydir.update(userheight.split("Height : ", userheight))

mylist.append(username)
mylist.append(userage)
mylist.append(userheight)
print(mylist)
