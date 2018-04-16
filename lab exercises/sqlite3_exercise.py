import sqlite3
import time

connection = None
cursor = None

def connect(path):
	global connection, cursor

	connection = sqlite3.connect('/cshome/xianhang/C291/register.db')

	# TODO: Create and populate table is the database using 'init.sql' (from eclass)
	cursor = connection.cursor()

	file_object = open('lab4.sql')
	file_context = file_object.readline()
	file_str = ''.join(file_context)

	cursor.executescript(file_str)

	cursor.execute(' PRAGMA forteign_keys=ON; ')
	connection.commit()

	return

def createEnrollTable():

	global connection, cursor

	# TODO: create a table enroll (studentID, courseID, term, grade) 
	connect(path)
	table = "create table enroll (\
  		studentID 		int,\
  		courseID		text,\
  		term			text,\
  		grade			int,\
  		primary key (term,studentID,courseID),\
  		foreign key (studentID) references students (studentID)\
		foreign key (courseID) references courses(courseID));"
	
	cursor.execute(table)
	connection.commit()
	
	return 


def checkSeatsAvailable(course_id):

	global connection, cursor

	# Write your code here
	connect(path)
	cursor = connection.cursor()
	
	check = ('course_id')
	connection.execute('SELECT * FROM courses WHERE symbol=? AND qty>?',check)	

	row = cursor.fetchone()
	print row.keys()			
	rows = cursor.fetchall()
	for row in rows:
		print row["qty"]


	return


def enroll(student_id, course_id):
	
	global connection, cursor

	current_term = "Winter 2018"
 
	# TODO: Check that there is a spot in the course for this student.
	# TODO: Register the student in the course.
	# TODO: Update the seats_available in the course table. (decrement)

	return


def generateTranscript(student_id):

	global connection, cursor

	# Write your code here

	return


def main():
	global connection, cursor

	path="./register.db"
	connect(path)

	createEnrollTable()

	while True:

		student_id = input('Please enter the student ID or q to exit: ')
		if student_id == 'q':
			break

		course_id = input('Please enter the course ID: ')
		if course_id == 'q':
			break

		enroll(student_id, course_id)
		generateTranscript(student_id)


	return


if __name__ == "__main__":
	main()
