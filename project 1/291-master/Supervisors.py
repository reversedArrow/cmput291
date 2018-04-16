import sqlite3
from AccountManager import AccountManager

class Supervisor:
	def __init__(self, user_id, conn, cursor):
		self.user_id = user_id
		self.conn = conn
		self.cursor = cursor

	def supervisor_menu(self):
		while True:
			option = int(input('''select task\n
			1. Create new account.\n
			2. Create a new master account with all the required information.\n
			3. For a given customer, add a new service agreement with all the required information -except for the master account number, and the service_no, which should be automatically filled in by the system; master_account is the number of the selected customer, and the service_no is a running numbers, so the next available number should be filled in.\n
			4. log out\n'''))
			if option == 1:
				self.task1()
			elif option == 2:
				self.task2()
			elif option == 3:
				self.task3()  
			elif option == 4:
				return
	
	def task1(self):
		self.cursor = self.conn.cursor()
	
		# display all account managers under current supervisor
		self.cursor.execute('''
							select p.pid
							from personnel p
							where p.supervisor_pid = :supervisor_id
							and p.pid in (
							select pid from account_managers)
							''',
							{"supervisor_id": self.user_id}
							)
		# select one account manager's ID
		rows = self.cursor.fetchall()
		available_account_mgr = set()
		
		print("Select an account manager listed below: ")
		for row in rows:
			print(row[0])
			available_account_mgr.add(row[0])

		# select an account
		while True:
			mgr_id = input("Select an account manager ID: ")
			if mgr_id in available_account_mgr:
				break
			else:
				print("The account manager is not under current supervisor!") 

		am = AccountManager(mgr_id, self.conn, self.cursor)
		am.task2()

	def task2(self):
		try:
			self.cursor = self.conn.cursor()

			# display all customers of all account managers that the supervisor supervises
			self.cursor.execute('''
				select account_no 
				from accounts
				where account_mgr in
				(
				select p.pid
				from personnel p
				where p.supervisor_pid = :supervisor_id
				and p.pid in (
				select pid from account_managers)
				)''',
				{"supervisor_id": self.user_id}
				)
			rows = self.cursor.fetchall()
			available_customer = set()
			print("Available customers: ")
			for row in rows:
				print(row[0])
				available_customer.add(int(row[0]))

			# select a customer
			while True:
				acct_id = int(input("Select an account ID above: "))
				if acct_id not in available_customer:
					print("Account not available! Select again!")
				else:
					break

			# select this customer's account manager
			self.cursor.execute('''
				select account_mgr 
				from accounts
				where account_no = :acct_id
				''',
				{"acct_id": acct_id}
				)	
			row = self.cursor.fetchone()	
			acct_mr = row[0]	

			# create summary report
			self.cursor.execute('''
								select count(sa.service_no), sum(sa.price), sum(sa.internal_cost), count(distinct sa.waste_type)
								from service_agreements sa
								where sa.master_account = :acct_id
								group by sa.master_account
								''',
								{"acct_id": acct_id})    
			rows = self.cursor.fetchall()
			
			print('acct_manager, no_of_service_agreements  price_sum  internal_cost_sum  num_of_different_waste_types')
			for row in rows:
				print(acct_mr,row[0],row[1],row[2],row[3])

		except:
			print("An unexpected error occur!")


	def task3(self):
		try:
			self.cursor = self.conn.cursor()

			self.cursor.execute('''
				select a.account_mgr, count(sa.master_account),sum(sa.price),sum(sa.internal_cost)
				from accounts a, service_agreements sa
				where a.account_no = sa.master_account
				and account_mgr in
				    (select p.pid
				    from personnel p
				    where p.supervisor_pid = :supervisor_id
				    and p.pid in (
				    select pid from account_managers))
				group by account_mgr
				order by sum(sa.price)-sum(sa.internal_cost)
				''',
				{"supervisor_id": self.user_id})

			rows = self.cursor.fetchall()
			for row in rows:
				print(row)
		except:
			print("An unexpected error occur!")
