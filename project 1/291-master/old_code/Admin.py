import sqlite3

class Admin:

    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    def __init__(self, staff_id, conn, cursor):
        self.staff_id = staff_id
        self.conn = conn
        self.cursor = cursor


    def admin_menu(self):
        while True:
            choice = int(raw_input('''Select task\n
                                1. List drugs that the doctor prescribed in specified period of time.\n
                                2. List total amount prescribed for each drug in that category in a specified period of time.\n
                                3. List all possible medications for a given diagnosis.\n
                                4. List for a given drug all the diagnoses that have been made before prescribing the drug.\n
                                5. Log out\n'''))

            if choice == 5:
                return

            if choice == 1:
                self.task1()
            elif choice == 2:
                self.task2()
            elif choice == 3:
                self.task3()
            elif choice == 4:
                self.task4()

    def task1(self):

        print "Specify time periods in YYYY-MM-DD HH:MM:SS"

        start_time = raw_input("Specify starting time >")
        end_time = raw_input("Specify ending time >")

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute('''SELECT s.name, m.drug_name, SUM(m.amount)
        				 FROM medications m, staff s
        				 WHERE m.staff_id = s.staff_id
        				 AND m.mdate >= :start_time
        				 AND m.mdate <= :end_time
        				 GROUP BY m.staff_id, m.drug_name''', {"start_time": start_time, "end_time": end_time})

            rows = self.cursor.fetchall()

            print rows

        except sqlite3.Error as e:
            print e.message
            return -1

    def task2(self):

        print "Specify time periods in YYYY-MM-DD HH:MM:SS"

        start_time = raw_input("Specify starting time >")
        end_time = raw_input("Specify ending time >")

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute('''SELECT d.category, SUM(m.amount)
                              FROM drugs d, medications m
                              WHERE d.drug_name = m.drug_name
                              AND m.mdate >= :start_time
                              AND m.mdate <= :end_time
                              GROUP BY d.category''', {"start_time": start_time, "end_time": end_time})
            rows1 = self.cursor.fetchall()

            print rows1

            self.cursor = self.conn.cursor()
            self.cursor.execute('''SELECT m.drug_name, SUM(m.amount), d.category
                                   FROM medications m, drugs d
                                   WHERE m.drug_name = d.drug_name
                                   AND m.mdate >= :start_time
                                   AND m.mdate <= :end_time
                                   GROUP BY m.drug_name''', {"start_time": start_time, "end_time": end_time})
            rows2 = self.cursor.fetchall()

            print rows2



        except sqlite3.Error as e:
            print e.message
            return -1

    def task3(self):

        diagnosis = raw_input("Specify diagnosis >")

        try:
            self.cursor = self.conn.cursor()

            self.cursor.execute('''SELECT m.drug_name
                         FROM medications m, diagnoses d
                         WHERE d.diagnosis = :diagnosis
                         AND m.hcno = d.hcno
                         AND m.mdate > d.ddate
                         GROUP BY m.drug_name
                         ORDER BY COUNT(m.drug_name) DESC ''', {"diagnosis": diagnosis})

            rows = self.cursor.fetchall()

            print rows

        except sqlite3.Error as e:
            print e.message

    def task4(self):

        drug_name = raw_input("Specify the name of drug >")

        try:
            self.cursor = self.conn.cursor()

            self.cursor.execute('''SELECT d.diagnosis
                         FROM diagnoses d, medications m
                         WHERE m.drug_name = :drug_name
                         AND m.chart_id = d.chart_id
                         AND d.ddate < m.mdate
                         GROUP BY diagnosis
                         ORDER BY AVG(m.amount)''', {"drug_name": drug_name})

            rows = self.cursor.fetchall()

            print rows

        except sqlite3.Error as e:
            print e.message
