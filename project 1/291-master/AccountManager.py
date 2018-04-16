import sqlite3

class AccountManager:

	def __init__(self, user_id, conn, cursor):
		self.user_id = user_id
		self.conn = conn
		self.cursor = cursor

	def menu(self):
		while True:
			option = int(input('''select task\n
			1. Select a customer and list all the information associated with this customer, followed by the list of all the individual service agreements under for this customer, ordered by service_no.\n
			2. Create a new master account with all the required information.\n
			3. For a given customer, add a new service agreement with all the required information -except for the master account number, and the service_no, which should be automatically filled in by the system; master_account is the number of the selected customer, and the service_no is a running numbers, so the next available number should be filled in.\n
			4. Create a summary report for a single customer, listing the total number of service agreements, the sum of the prices and the sum of the internal cost of the service agreements, as well as the number of different waste types that occur in the service agreements.\n
			5. log out\n'''))
			if option == 1:
				self.task1()
			elif option == 2:
				self.task2()
			elif option == 3:
				self.task3()       	 
			elif option == 4:
				self.task4()
			elif option == 5:
				return      	 

	def task1(self):  
		
		print("Select a customer below: ")

		self.cursor.execute('''
							select a.account_no
							from accounts a
							where a.account_mgr = :manager_id
							''',
							{"manager_id": self.user_id,})

		rows = self.cursor.fetchall()
		for row in rows:
			print(row[0])

		input_master_account = int(input("Select a customer above: "))

		self.cursor.execute('''
							select a.account_no
							from accounts a
							where a.account_mgr = :manager_id
							and a.account_no = :input_master_account
							''',
							{"manager_id": self.user_id,
							"input_master_account": input_master_account})
		
		row = self.cursor.fetchone()
		if row is None:
			print("This account is not managed by the current manager!")
			return

		print("Customer Information: ")
		self.cursor.execute('''
							select *
							from accounts
							where account_no = :input_master_account
							''',
							{"input_master_account": input_master_account})

		row = self.cursor.fetchone()
		print("account_no account_mgr customer_name contact_info customer_type start_date end_date total_amount") 
		print(row)
		print()

		print("Customer's service agreements: ")
			
		self.cursor.execute('''
							select *
							from service_agreements sa
							where sa.master_account = :input_master_account
							order by sa.service_no
							''',
							{"input_master_account": input_master_account})
		rows = self.cursor.fetchall()
		if rows == []:
			print("This customer does not have any service agreement record.")
		else:
			for row in rows:
				print(row)

	def task2(self):

		self.cursor = self.conn.cursor()
		
		input_account_no = input("Enter customer's account_no: ")	
		# error handling: when master account already exists
		self.cursor.execute('''
							select *
							from accounts 
							where account_no = :input_account_no 
							''',
							{"input_account_no": input_account_no}
							)
		row = self.cursor.fetchone()
		if row is not None:
			print("Account already exists!")
			return

		# error handling: when customer type does not exist
		while True:
			input_customer_type = input("Enter customer's customer_type(municipal/commercial/industrial/residential): ")
			if input_customer_type!="municipal" and input_customer_type!="commercial" and input_customer_type!="industrial" and input_customer_type!="residential":
				print("Customer type not valid!")
			else:
				break

		input_customer_name = input("Enter customer's name: ")
		input_contact_info = input("Enter customer's contact_info: ")
		input_start_date = input("Enter customer's start date(YYYY-MM-DD): ")
		input_end_date = input("Enter customer's end date(YYYY-MM-DD): ")

		# add to accounts table
		self.cursor.execute('''
						   insert into accounts
						   values (?, ?, ?, ?, ?, ?, ?, ?)
						   ''', 
						   (input_account_no, 
							self.user_id, 
							input_customer_name, 
							input_contact_info, 
							input_customer_type, 
							input_start_date, 
							input_end_date,
							0)
						   )
		
		self.conn.commit()
		print("data insert successfully")

	def task3(self):
 
		try:
			self.cursor = self.conn.cursor()

			while True:

				# find all accounts the account manager manages
				self.cursor.execute('''
									select a.account_no 
									from accounts a
									where account_mgr = :mgr_id
									''',
									{"mgr_id": self.user_id}
									)
				
				rows = self.cursor.fetchall()
				
				# select an account
				print("Select an account no listed below: ")
				
				available_accounts = set()
				for row in rows:
					print(row[0])
					available_accounts.add(row[0])
				input_account = input("Enter account: ")

				# if the account not one of available accounts
				if input_account not in available_accounts:
					print("Selected account is not managed by the current manager!")
				else:
					break

			# get user input for new service agreement
			input_location = input("Enter the location: ")
			
			waste_type_options = {"hazardous waste",
									"mixed waste",
									"construction waste",
									"metal",
									"compost",
									"paper",
									"plastic"}
			while True:
				input_waste_type = input("Enter the waste_type: ")
				if input_waste_type in waste_type_options:
					break
				print("Unsupported waster type! Try again!")
			
			input_pick_up_schedule = input("Enter the pick_up_schedule: ")
			input_local_contact = input("Enter the local_contact: ")
			input_internal_cost = input("Enter the internal_cost: ")
			input_price = input("Enter the price: ")			

			# find largest service number in table
			self.cursor.execute('''
								select service_no
								from service_agreements
								''')
			largest = 0
			rows = self.cursor.fetchall()
			for row in rows:
				if int(row[0]) > largest:
					largest = int(row[0])
			service_no = largest + 1

			# create new service agreement
			self.cursor.execute('''
							   insert into service_agreements
							   values (?, ?, ?, ?, ?, ?, ?, ?)
							   ''', 
							   (service_no, 
								input_account,
								input_location, 
								input_waste_type, 
								input_pick_up_schedule, 
								input_local_contact, 
								input_internal_cost,
								input_price)
							   )
			self.conn.commit()
			
			# update account's total amount
			# get the original amount
			self.cursor.execute('''
								select total_amount
								from accounts
								where account_no = :input_account
								''',
								{"input_account": input_account})
			row = self.cursor.fetchone()
			updated_amt = row[0] + float(input_price)

			# compute updated amount
			self.cursor.execute('''
								update accounts
								set total_amount = :updated_amt
								where account_no = :input_account
								''',
								{"input_account": input_account,
								"updated_amt": updated_amt
								})
			self.conn.commit()

		except:
			print("An unexpected error occur!")

	def task4(self):		
		try:

			print("Select a customer below: ")

			self.cursor.execute('''
								select a.account_no
								from accounts a
								where a.account_mgr = :manager_id
								''',
								{"manager_id": self.user_id,})

			rows = self.cursor.fetchall()
			for row in rows:
				print(row[0])

			input_master_account = int(input("Select a customer: "))

			self.cursor = self.conn.cursor()
			
			self.cursor.execute('''
								select count(sa.service_no), sum(sa.price), sum(sa.internal_cost), count(distinct sa.waste_type)
								from service_agreements sa
								where sa.master_account = :input_master_account
								group by sa.master_account
								''',
								{"input_master_account": input_master_account})    
			rows = self.cursor.fetchall()

			self.cursor.execute('''
								select a.account_no
								from accounts a
								where a.account_mgr = :manager_id
								and a.account_no = :input_master_account
								''',
								{"manager_id": self.user_id,
								"input_master_account": input_master_account})
			
			row = self.cursor.fetchone()
			if row is None:
				print("This account is not managed by the current manager!")
				return

			print('no_of_service_agreements  price_sum  internal_cost_sum  num_of_different_waste_types')
			
			if rows != []:
				for row in rows:
					print(row[0],row[1],row[2],row[3])
			else:
				print(0,0,0,0)
		
		except:
			print("An unexpected error occur!")


