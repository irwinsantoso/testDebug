#Debug this program !

class User():

	def __init__(self,username,password,nik,age,):
		self.username = username
		self.password = password
		self.nik = nik
		self.age = age

	def CekUmurLegal(self):
                if(self.age<21):
                        print("kamu masih belum cukup umur")
		else:
			print(welcome to the real world)

	def Login(self,username,password)
		if(self.username==username and self.password==password):
			print("Login successfull")
			return "succes"
		else:
			print("Sorry, incorrect username or password")
			return "unsuccess"


user1 = User("irwinSan","changeyourpwd","19021",'27')

status = user1.Login("irwinSan","changeyourpwd")
if (status=="success"):
	print ("Hello "+user1.username)
	user1.CekUmurLegal()
	print("Congratulations, you have passed the test !")
else:
	print("Nope,not yet")
