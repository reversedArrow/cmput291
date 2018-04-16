import sqlite3
from Drivers import Driver
from AccountManager import AccountManager
from Dispatchers import Dispatcher
from Supervisor import Supervisor
from check import check
from hashlib import pbkdf2_hmac
import sys
def pwdHash(password):
	hash_name = 'sha256'
	salt = 'ssdirf993lksiqb4'
	iterations = 100000
	dk = pbkdf2_hmac(hash_name, bytearray(password, 'ascii'), bytearray(salt, 'ascii'), iterations)
	return dk 


def sign_in():
	username = input("enter username(enter new to sign up or q to quit): ")
	if username == 'new':
		sign_up()
	elif username == 'q':
		sys.exit()
	pa = input("enter password: ")
	password = pwdHash(pa)

	x = check()
	pas = x.checkPassword(username,password)
	user_id = []

	if pas:
		role = x.check_role(username,password) # ask for role
		print('\n')
		print("Welcome,"+role)
		print('\n')
		return role
	else:
		print("Invalid login!")
		print('\n')
		flag = input("do you want to sign up? (enter y for sign up, q for log out, n for return to menu): ")
		if flag == 'y' or flag =='Y':	
			sign_up()
		elif flag == 'n' or flag =='N':
			return		
		elif flag == 'q' or flag =='Q':
			sys.exit() 

	


def sign_up():
	
	while True:
		
		username = input("Please enter your username, enter q to exit: ")
		x = check()
	
		if username == 'q':
			sys.exit() 
		
		while username in x.check_exist_username():
			print("this username has been taken!")
			return
		pas = input("Please enter your password: ")
		password = pwdHash(pas)
		roleList = ["dispatcher","driver","supervisor","account_manager"]
		
		flag = True

		while flag:
			
			pid = input("Please enter your personnel ID: ")
			while pid not in x.check_personnel_id():
				print("personnel ID does not exist or has been taken.")
				return
			role = input("enter your role: ")
			if role == "Driver":
				x.creat_data_for_newuser(pid,username,password,role)
				print('account creat successfull')
				return
			if role == "Account Manager":
				x.creat_data_for_newuser(pid,username,password,role)
				print('account creat successfull')
				return
			if role == "Supervisor":
				x.creat_data_for_newuser(pid,username,password,role)
				print('account creat successfull')
				return
			if role == "Dispatcher":
				x.creat_data_for_newuser(pid,username,password,role)
				print('account creat successfull')
	
				return
			elif role != roleList[0] and role != roleList[1] and role != roleList[2] and role != roleList[3]:
				print("Please enter the correct role!")
				return
	

		return
  
if __name__ == "__main__":

	conn = sqlite3.connect('waste_management.db')
	cursor = conn.cursor()

	# menu()
	
	while 1:
		menu = input("Hello, How are you? Enter 1 to log in , 2 to sign up, 3 to exit: ")
		menu = int(menu)
		if menu == 1:
			y = check()
			user_id = y.getUser_id()
			username = y.getusername()
			driver_id = y.getdriver_id()

			role = sign_in()
			if role == 'Dispatcher':
				
				dispatcher = Dispatcher(user_id, conn, cursor)
				dispatcher.dispatcher_menu()
			elif role == 'Account Manager':
				accountManager = AccountManager(username, conn, cursor)
				accountManager.menu()  
			elif role == 'Driver':
				driver = Driver(driver_id, conn, cursor)
				driver.driver_menu()    
			elif role == 'Supervisor':
				supervisor = Supervisor(user_id, conn, cursor)
				supervisor.supervisor_menu()
		elif menu == 2:
			sign_up()
		elif menu == 3:
			sys.exit()
	# print(role)
	