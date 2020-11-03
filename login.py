import user as us
import json

def Error(): 
	print("Error,Unable to login")

Running = True

objList = []

while(Running):
	LoginOrSignup = input("Are you an existing user : ").lower()

	if(LoginOrSignup == "no" or LoginOrSignup == "n"):
		name = input("Enter Your name : ")
		username = input("Enter Your username : ")
		userCheck = us.user.checkForUsername(username,objList)
		if (userCheck==True):
			print("This account already exists")
		
		else:
			password = input("Enter your password : ")
			userInfo = us.user(username,password,name)
			objList.append(userInfo)
			print("account successfully created")


	elif(LoginOrSignup == "yes" or LoginOrSignup == "y"):
		username = input("Enter your username : ")
		user = us.user.checkForExistingUser(objList,username)
		if(user == None):
			print("------------------------------------------------------")
			print("It seems you dont have an account here,go create one!!")
		else:
			for x in range(0,5):
				password = input("enter the password : ")
				verify = us.user.checkForPassword(user,password)
				if(verify):
					print("----------------------")
					print("Logged in successfully as "+user.name)
					break
				else:
					print("-------------------")
					print("incorrect password")
	else:
		print("Please Enter in Yes or No")
