#!/usr/bin/python3 
print("content-type:text/html")
print()

import cgi
import subprocess as sp

name=(cgi.FieldStorage()).getvalue("usid")
pd=(cgi.FieldStorage()).getvalue("pwd")
cmnd=(cgi.FieldStorage()).getvalue("cmd")
option=(cgi.FieldStorage()).getvalue("opt")
fname=(cgi.FieldStorage()).getvalue("fname")


if pd=="RedHAT8@entry":
	print("HIIIII    "+name+"\n")
	print()
	print("WELCOME to Redhat8 Command Output portal !!! \n")
	if cmnd=="df -h" or option=="df -h":
		s=sp.getstatusoutput("df -h")
		if s[0]==0:
			print("THE STORAGE DETAILS ARE as follows :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="free -m" or option=="free -m":
		s=sp.getstatusoutput("free -m")
		if s[0]==0:
			print("THE MEMORY MANAGEMENT DETAILS ARE as follows :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="ifconfig" or option=="ifconfig":
		s=sp.getstatusoutput("ifconfig")
		if s[0]==0:
			print("THE NETWORK DETAILS ARE as follows :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="mkdir" or option=="mkdir":
		s=sp.getstatusoutput("sudo mkdir {}".format(fname))
		if s[0]==0:
			print("Your new directory has been created !!! \n")
			print("Here are the list of files and folders !!! \n\n")
			print(sp.getoutput("ls"))
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="ls" or option=="ls":
		s=sp.getstatusoutput("ls")
		if s[0]==0:
			print("The list of all files and folders are as follows :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="date" or option=="date":
		s=sp.getstatusoutput("date")
		if s[0]==0:
			print("Today's DATE and TIME :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")
	if cmnd=="cal" or option=="cal":
		s=sp.getstatusoutput("cal")
		if s[0]==0:
			print("The calender of this month :\n")
			print(s[1])
		else:
			print("An Unexpected ERROR occured .... Sorry for the INCOVINIENCE !!!")

else :
	print("INVALID PASSWORD !!! ... Try Again... ")
		
	
		
		




   

    
		
		
	
