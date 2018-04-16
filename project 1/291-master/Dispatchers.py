import sqlite3

class Dispatcher:

    def __init__(self,user_id,conn,cursor):
        self.conn = conn
        self.cursor = cursor        
        
    def dispatcher_menu(self):

        while True:
            choice = int(input('''Select task\n
                                1. Create an entry in service fulfillments\n
                                2. Log out\n'''))

            if choice == 1:
                self.select_agreement()
            elif choice == 2:
                return         
            
    def select_agreement(self):

        while True:
            choice = int(input('''Create an entry in service fulfillments\n
                                1. List service aggreemeents\n
                                2. Input for service fulfillments\n
                                3. Go Back\n'''))

            if choice == 1:

                self.cursor = self.conn.cursor()

                # print out all sa;
                # remind user to select an agreement and also provide an entry to log out
                self.cursor.execute(''' select *
                                        from service_agreements sa;
                                    ''')
                rows = self.cursor.fetchall()

                for row in rows:
                    print (row[0], " ", row[1], "    ", row[2], "    ", row[3], "    ", row[4], "    ", row[5], "    ", row[6], "    ", row[7])

                # print row
                print ("\n")

            elif choice == 2:
                self.task2()
            elif choice == 3:
                return

    def task2(self):

        while True:

            input_service_no = int(input('''Enter Service Number:\n'''))

            self.cursor.execute('''select * from service_agreements sa where sa.service_no = :input_service_no;''',  {"input_service_no": input_service_no})
            results = self.cursor.fetchall()

            if results == []:
                print ("service number does not exist!")
                break

            input_driver_id = int(input('''Enter Driver Id:\n'''))
            self.cursor.execute('''select * from drivers d where d.pid == :input_driver_id;''',  {"input_driver_id": input_driver_id})
            results = self.cursor.fetchall()

            if results == []:
                print ("driver id does not exist!")
                break

            self.cursor.execute('''select owned_truck_id from drivers d where d.pid=:input_driver_id;''',{"input_driver_id":input_driver_id})
            results = self.cursor.fetchall()
            if results[0][0] is not None:
                input_truck_id = results[0][0]
                print ("truck " + input_truck_id + " is owned by this driver")
            else:
                input_truck_id = int(input('''Enter Truck Id:\n'''))
                self.cursor.execute('''select truck_id from trucks where truck_id not in 
                    (select owned_truck_id from drivers where owned_truck_id is not NULL) and truck_id = :input_truck_id;''', {"input_truck_id":input_truck_id})
                results = self.cursor.fetchall()
                if results != []:
                    print ("truck " + str(input_truck_id) + " can be assigned to this driver")
                else:
                    print ("truck id does not exist!")
                    break

            print ("input_service_no,    driver_id,     truck_id")
            print (str(input_driver_id) + "  " + str(input_driver_id) + "    " + str(input_truck_id))

            date_time = input("Enter a date (YYYY-MM-DD): ")

            self.cursor.execute("select master_account from service_agreements where service_no=:input_service_no",{"input_service_no":input_service_no})
            result=self.cursor.fetchone()
            master_account = result[0]

            self.cursor.execute('''SELECT cid_drop_off
                        FROM service_fulfillments sf
                        WHERE sf.master_account = :accn
                        AND sf.service_no = :servn
                        AND julianday(:dat) - julianday(sf.date_time) > 0
                        ORDER BY julianday(:dat) - julianday(sf.date_time)''', {"accn":master_account,"servn":input_service_no, "dat":date_time})
            
            result = self.cursor.fetchone()
            if result is not None:
                cid_pick_up = result[0]
            else:
                cid_pick_up = None

            self.cursor.execute('''SELECT container_id FROM container_waste_types
                        WHERE waste_type IN (SELECT sa.waste_type FROM service_agreements sa
                                            WHERE sa.master_account = :ma AND sa.service_no = :sn)
                        AND container_id IN (SELECT container_id FROM containers
                                            WHERE (SELECT COUNT(*) FROM service_fulfillments
                                                    WHERE cid_drop_off = container_id) =
                                                    (SELECT COUNT(*) FROM service_fulfillments
                                                    WHERE cid_pick_up = container_id))
                        AND container_id NOT IN (SELECT cid_drop_off FROM service_fulfillments
                                                WHERE julianday(:dt) - julianday(date_time) < 0)''', {"ma":master_account, "sn":input_service_no, "dt":date_time})
            results = self.cursor.fetchall()

            for result in results:
                print (result)

            cid_drop_off = int(input('''Enter Container Id to drop off:\n'''))

            try:

                self.cursor.execute('''INSERT INTO service_fulfillments VALUES (?,?,?,?,?,?,?)''', (date_time, master_account, input_service_no,
                        input_truck_id, input_driver_id, cid_drop_off, cid_pick_up))
                self.conn.commit()
                print("Entry inserted!")

            except sqlite3.Error as e:
                print (e.message)
