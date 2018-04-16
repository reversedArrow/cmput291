# Name: Xianhang Li
# CCID: 1465904

import sys
import sqlite3
import time
from random import randint
import datetime

# connection = None
cursor = None
connection = sqlite3.connect('lab_exam_2.db')

# Your functions go here
# ======================
def add_flight():
	unique = True
	while unique:
		flight_id = str(randint(11,100))
		if check_unique_id(flight_id):
			break

	flight_id = str(randint(11,100))
	source = input("Please enter source: ")
	destination = input("Please enter destination: ")
	departure_date = input("Please enter departure date: ")
	airline_name = input("Please enter airline name: ")
	capacity = input("Please enter capacity: ")

	try:
		c = connection.cursor()
		c.execute('''INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?)''',(flight_id, source, destination, departure_date, airline_name, capacity,))
		connection.commit()
		print("Add successfull")
	except sqlite3.Error as e:
		print ("Error: " + e.message)

	return
def check_unique_id(flight_id):
	c = connection.cursor()
	c.execute('''SELECT * FROM flight WHERE flight_id = ?''', (flight_id,) )
	row = c.fetchall()
	if not row:
		return True

def search_flight():
	destination = input("Please enter destination: ")
	c = connection.cursor()
	c.execute('''SELECT * FROM flight WHERE destination = ?''', (destination,) )
	rows = c.fetchall()
	for row in rows:
		print(row[0],row[1],row[2],row[3],row[4],row[5])

	return

def book_flight():
	c = connection.cursor()
	date = datetime.date.today()
	c.connection.cursor()
	c.execute('''SELECT flight_id FROM flight''')
	rows = c.fetchall()
	for row in rows:
		print(row)
	passenger_id = input("Please enter your passenger id: ")
	flight_id = input("Please enter the flight id you want to book: ")
	flight_class = input("Please select your class(ECO,BUS,FIR): ")
	if check_avaliable_seat(flight_id):

		c.execute('''INSERT OR IGNORE INTO reserve VALUES (?, ?, ?, ?)''', (passenger_id, flight_id, flight_class, date))
		connection.commit()
		print("You have successfull booked your flight!")
		update_avaliable_seat(flight_id)
	else:
		return


def check_avaliable_seat(flight_id):
	c = connection.cursor()
	c.connection.cursor()
	c.execute('''select f.current_capacity from flight f where f.flight_id = ?''',(flight_id,))
	rows = c.fetchall()
	if rows:
		if rows[0][0] == 0:
			return False
		else:
			return True


def update_avaliable_seat(flight_id):
	c = connection.cursor()
	c.connection.cursor()
	c.execute('''SELECT current_capacity FROM flight WHERE flight_id = ?''', (flight_id,))
	row = c.fetchall()
	capacity = row[0][-1]
	capacity -= 1
	c.execute('''UPDATE flight set current_capacity = ? where flight_id = ?''',(capacity,flight_id))
	connection.commit()
	print("Book successfull")

	return

def cancel_flight():
	c = connection.cursor()
	c.connection.cursor()
	c.execute('''select fl_id from reserve''')
	rows = c.fetchall()
	for row in rows:
		print(row)
	ps_id = input("Please enter your passenger id: ")
	fl_id = input("which flight do you want to cancell: ")
	c.execute('''DELETE FROM reserve WHERE ps_id = ? and fl_id = ?''',(ps_id,fl_id))
	connection.commit()
	update_avaliable_seat2(fl_id)

	return

def update_avaliable_seat2(fl_id):
	c = connection.cursor()
	c.connection.cursor()
	c.execute('''SELECT current_capacity FROM flight WHERE flight_id = ?''', (fl_id,))
	row = c.fetchall()
	capacity = row[0][-1]
	capacity += 1
	c.execute('''UPDATE flight set current_capacity = ? where flight_id = ?''',(capacity,fl_id) )
	connection.commit()
	print("Cancell successfull")

	return





def printMenu():

	date = datetime.date.today()

	while(True):

		print("\nPlease select an option:")
		print("1 - Add a new flight")
		print("2 - Search flights by destination")
		print("3 - Book a flight")
		print("4 - Cancel a flight")
		print("5 - Exit")

		selectedOption = input("you want to do option ")
		selectedOption = int(selectedOption)
		

		

		try:
			selectedOption = int(selectedOption)


			if selectedOption > 0 and selectedOption < 6:
				return selectedOption

			print ("Invalid option")

		except:
			
			print ("Invalid option")

	return


def connect(path):
	global connection, cursor

	connection = sqlite3.connect(path)
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute(' PRAGMA forteign_keys=ON; ')

	initScript = open('init.sql', 'r').read()
	cursor.executescript(initScript)

	connection.commit()

	return

	
def main():
	global connection, cursor

	path = "./lab_exam_2.db"
	pathInitFile = "./init.sql"
	date = datetime.date.today()
	connect(path)
	# your call to the function that initializes the global variables

	
	# your call to the funtion that creates and populates the tables using init.sql

	while (True):

		userOption = printMenu()
		if userOption == 1:
			add_flight()
		if userOption == 2:
			search_flight()
		if userOption == 3:
			book_flight()
		if userOption == 4:
			cancel_flight()
		if userOption == 5:
			sys.exit()
		
		# Your code for handling the different options; it must be based on calling 
		# the functions that you are required to write accoring to the lab exam specifications. 

	return



if __name__ == "__main__":
	main()
