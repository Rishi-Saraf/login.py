class user:
	def __init__(self,username,password,name):
		self.username = username
		self.password = password
		self.name = name

	@staticmethod
	def checkForPassword(obj,password):
		if(obj.password == password):
			return True
		else:
			return False

	@staticmethod
	def checkForExistingUser(array,username):
		for x in array:
			if(x.username == username):
				return x
		return None


	@staticmethod
	def checkForUsername(username,array):
		for x in array:
			if(x.username == username):
				return True;
			else:
				return False

