import sqlite3

class Driver:

	def __init__(self, driver_id, conn, cursor):
		self.driver_id = driver_id
		self.conn = conn
		self.cursor = cursor

	def driver_menu(self):
		while True:
			choice = int(input('''Select task\n
				1. List driver's assigned tours\n
				2. Log out\n'''))

			if choice == 2:
				return

			if choice == 1:
				self.task1()

	def task1(self):
		
		start_date = input("Specify start date >")
		end_date = input("Specify end date >")

		try:
			self.cursor = self.conn.cursor()

			self.cursor.execute('''SELECT sa.location, sa.local_contact, sa.waste_type, sf.cid_drop_off, sf.cid_pick_up
								FROM service_fulfillments sf, service_agreements sa
								WHERE sf.driver_id = :driver_id
								AND sf.master_account = sa.master_account
								AND sf.service_no = sa.service_no
								AND sf.date_time > :start_date 
								AND sf.date_time < :end_date''',
								{"driver_id": self.driver_id,
								 "start_date": start_date,
								 "end_date": end_date})

			rows = self.cursor.fetchall()

			print('location   contact   waste type    drop off    pick up')
			for row in rows:
				print(row)

		except:
			print("Unexpected error occurred!")

