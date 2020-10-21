#!/usr/bin/python3

############
##Script details & function::
#Script Name - BckupNix
#Version - 001
#Written in Python3
#License - MIT License
#Creator - Max Williams
#Creation date - 10/18/2020
#Script Location - https://github.com/maxmit/BckupNix
#Script Documentation - https://maxmit.github.io/BckInfo/

#Script Function:
#To clean up multiple files and folders 
#all into one location of the person's choosing
#can be used as a backup script 
############

#load the following modules
import os
import shutil

lis = [] #this is a empty array/python list
i = 0 #this is a varible to use later in our while loop

#this is the destination folder varible, meaning where the data will be
#copied to once script is completed. 
#It can be any folder, any destination, any name
destDir = '/home/user/Documents/CleanUp.now'

#while loop to check if the folder already exists
while os.path.exists(destDir): 
    #add all contents to destination folder
    #and add to variable name --> destDir
    destDir += str(i) 
    i+=1
os.makedirs(destDir) #if folder does NOT exist, create it

#List all the contents in your source folder (the folder
#where you are coping from).
lis = os.listdir('/home/user/Documents')

#a for loop to cycle through the list array (named - lis)
for x in lis: 
    print (x)
    if x ==__file__:
        continue
    
    #this function moves all the contents
    #into the variable name -> destDir
    shutil.move(x,destDir)


###############################
#MIT License

#Copyright (c) [2020] [Maxie(Max) Williams Jr]

#Permission is hereby granted, free of charge, to any person obtaining #a copy of this software and associated documentation files (the #"Software"), to deal in the Software without restriction, including #without limitation the rights to use, copy, modify, merge, publish, #distribute, sublicense, and/or sell copies of the Software, and to #permit persons to whom the Software is furnished to do so, subject to #the following conditions:

#The above copyright notice and this permission notice shall be #included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, #EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF #MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. #IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY #CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, #TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#MIT License
#https://choosealicense.com/licenses/mit/#

#Reference Link
#https://choosealicense.com/

#As recommended per research from this video
#https://www.youtube.com/watch?v=Q4GYrcca12c

########################



