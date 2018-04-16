import sqlite3
from Drivers import Driver
from AccountManager import AccountManager
from Dispatchers import Dispatcher
from Supervisors import Supervisor
from check import check
from hashlib import pbkdf2_hmac

if __name__ == "__main__":

	conn = sqlite3.connect('waste_management.db')
	cursor = conn.cursor()

	# dispatcher = Dispatcher(user_id, conn, cursor)
	# dispatcher.dispatcher_menu()

	# accountManager = AccountManager(1, conn, cursor)
	# accountManager.menu()  

	# driver = Driver(33250, conn, cursor)
	# driver.driver_menu()    
	supervisor = Supervisor(2, conn, cursor)
	supervisor.supervisor_menu()