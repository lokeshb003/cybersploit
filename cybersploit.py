""" Script created by Lokesh Balaji """
import subprocess
subprocess.call("./master.sh",shell=True)
subprocess.call("./banner.sh",shell=True)
option = int(input("Enter the option:"))
if(option == 0):
	subprocess.call("./msf.sh",shell=True)
	option2 = int(input("Enter the option :"))
	if(option2==0):
		subprocess.call("./android_meterpreter.sh",shell=True)
		choice = str(input("Do you want to fire up msfconsole? ( Y or N ):"))
		if(choice == 'Y' or choice == 'y'):
			subprocess.call("./console.sh",shell=True)
		elif(choice == 'N' or choice == 'n'):
			exit
		else:
			print("Wrong input given. Retry.")
	elif(option2==1):
		subprocess.call("./windows_meterpreter.sh",shell=True)
		choice = str(input("Do you want to fire up the msfconsole? ( Y or N ):"))
		if(choice == 'Y' or choice == 'y'):
			subprocess.call("./console.sh",shell=True)
		elif(choice == 'N' or choice == 'n'):
			exit
		else:
			print("You have entered the wrong option. Please Try again!")
	elif(option2==3):
		subprocess.call("./x64windows.sh",shell=True)
		choice = str(input("Do you want to fire up the msfconsole? ( Y or N ):"))
		if(choice == 'Y' or choice == 'y'):
			subprocess.call("./console.sh",shell=True)
		elif(choice == 'N' or choice == 'n'):
			exit
		else:
			print("You have entered the wrong option. Please Try again!")
	elif(option2==2):
		subprocess.call("./x64android.sh",shell=True)
		choice = str(input("Do you want to fire up the msfconsole? ( Y or N ):"))
		if(choice == 'Y' or choice == 'y'):
			subprocess.call("./console.sh",shell=True)
		elif(choice == 'N' or choice == 'n'):
			exit
		else:
			print("You have entered the wrong option. Please Try again!")
	elif(option2==4):
		subprocess.call("./apple_ios.sh",shell=True)
		choice = str(input("Do you want to fire up the msfconsole? ( Y or N ):"))
		if(choice == 'Y' or choice == 'y'):
			subprocess.call("./console.sh",shell=True)
		elif(choice == 'N' or choice == 'n'):
			exit
		else:
			print("You have entered the wrong option. Please Try again!")
		
elif(option == 1):
	exit
else:
	print("You have entered a wrong option. Try again !")



