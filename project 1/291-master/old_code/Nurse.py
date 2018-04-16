import sqlite3


class Nurse:
    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    def __init__(self,staff_id,conn,cursor):
        self.staff_id = staff_id
        self.conn = conn
        self.cursor = cursor

    def nurse_menu(self):
        while True:

            choice = int(raw_input('''Type integer of desired task\n
                         1. Create a new chart for a patient\n
                         2. Close the chart when the patient leaves the hospital\n
                         3. For a given patient, list all charts in the system.\n
                         4. For a given patient and an open chart of the patient add an entry for symptoms\n
                         5. Log out\n'''))
            if choice == 1: 
                self.create_new_chart()                    
            elif choice == 2:
                self.close_chart()
            elif choice == 3:
                self.list_chart()
            elif choice ==4:
                self.add_symp()
            elif choice == 5:
                return

    def list_chart(self):
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        hcno = raw_input("Enter patient's hcno to view this patient's charts: ")
        self.cursor.execute('''
                        select pa.hcno, ch.chart_id, ch.adate,
                                case when ch.edate is NULL then 'open'
                                else 'closed' end
                        from charts ch, patients pa
                        where ch.hcno = pa.hcno
                          and pa.hcno = :hcno
                        group by pa.hcno, ch.chart_id, ch.adate, ch.edate
                        order by ch.adate
                        ''', {"hcno": hcno})
        rows = self.cursor.fetchall()
        print "\nAll charts in the system (ordered by adate):"
        print "hcno     chart_id    adate       open/closed"
        for row in rows:
            print row[0], " ", row[1], "    ", row[2], "    ", row[3]
            # print row
        print "\n"

        select_chart = raw_input("Would you like to select a chart to view all associated entries?(Y/N)")
        if select_chart == "N":
            return
        elif select_chart == "Y":
            chart_id_sel = raw_input("Enter chart_id of the chart you'd like to select: ")

            self.cursor.execute('''
                                select *
                                from symptoms sy
                                where sy.chart_id = :chart_id_sel
                                order by sy.obs_date
                                ''', {"chart_id_sel": chart_id_sel})
            rows = self.cursor.fetchall()
            print "\nAll symptoms associated with the selected chart: "
            print "hcno chart_id    staff_id    osb_date    symptom"
            for row in rows:
                print row[0], " ", row[1], "    ", row[2], "    ", row[3], "    ", row[4]

            self.cursor.execute('''
                                   select *
                                   from diagnoses di
                                   where di.chart_id = :chart_id_sel
                                   order by di.ddate
                                   ''', {"chart_id_sel": chart_id_sel})
            rows = self.cursor.fetchall()
            print "\nAll diagnoses associated with the selected chart: "
            print "hcno chart_id    staff_id        ddate       diagnosis"
            for row in rows:
                print row[0], " ", row[1], "    ", row[2], "    ", row[3], "    ", row[4]

            self.cursor.execute('''
                                   select *
                                   from medications me
                                   where me.chart_id = :chart_id_sel
                                   order by me.mdate
                                   ''', {"chart_id_sel": chart_id_sel})
            rows = self.cursor.fetchall()
            print "\nAll medications associated with the selected chart: "
            print "hcno chart_id    staff_id        mdate       start_med       end_med         amount  drug_name"
            for row in rows:
                print row[0], " ", row[1], "    ", row[2], "    ", row[3],\
                        "    ", row[4], "    ", row[5], "    ", row[6], "   ", row[7]


    # 2. For a given patient and an open chart of the patient add an entry for symptoms. The date obs_date should be set
    # to the current date and time.
    # http://www.sqlitetutorial.net/sqlite-date/
    # http://stackoverflow.com/questions/15473325/inserting-current-date-and-time-in-sqlite-database
    def add_symp(self):
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        hcno = raw_input("To add an entry for symptoms, enter a patient's hcno: ")
        chart_id_op = raw_input("Also enter the chart_id of an open chart of the patient: ")
        symp2add = raw_input("Enter the symptom of this entry: ")

        self.cursor.execute('''
                                select pa.hcno, ch.chart_id
                                from patients pa, charts ch
                                where pa.hcno = ch.hcno
                                  and pa.hcno = :hcno
                                  and ch.chart_id = :chart_id_op
                                  and ch.edate is NULL
                                ''', {"hcno": hcno, "chart_id_op": chart_id_op})
        row = self.cursor.fetchone()
        if row is None:
            print "Invalid input."
            return

        hcno = row[0]
        chart_id_op = row[1]

        self.cursor.execute('''
                                insert into symptoms
                                values ('%s', %s, %s, datetime('now'), '%s')
                                ''' % (hcno, chart_id_op, self.staff_id, symp2add))
        self.conn.commit()

    def create_new_chart(self):
        patient_hcno = raw_input("The patient's hcno >")
            
        self.cursor.execute('''SELECT * 
                        FROM patients
                        WHERE patients.hcno =:phcno''',{"phcno":patient_hcno})
        data = self.cursor.fetchall()
        if len(data) == 0:
            #the patient not exists
            print "The patient is a newcomer. Please create a new chart for the patient firstly."
            p_name = raw_input("The patient's name >")
            p_age_group = raw_input("The patient's age_group >")
            p_address = raw_input("The patient's address >")
            p_phone = raw_input("The patient's phone >")
            p_emg_phone = raw_input("The patient's emg_phone >")
            self.cursor.execute('''INSERT INTO patients 
                                    VALUES (?,?,?,?,?,?)
                                      ''',(patient_hcno,p_name,p_age_group,p_address,p_phone,p_emg_phone))
            self.conn.commit()
        #create chart    
        print "Create a new chart for a patient."
        LastNumber = 1
        p_chart_id = patient_hcno+"_"+str(LastNumber)
        LastNumber = 1+LastNumber

        self.cursor.execute('''SELECT *
                            FROM charts
                            WHERE charts.chart_id = :pid''',{"pid":p_chart_id})
        data2 = self.cursor.fetchall()
        #check whether the chart_id is repeated
        while len(data2) != 0:
            p_chart_id = patient_hcno+"_"+str(LastNumber)
            LastNumber = 1+LastNumber
            self.cursor.execute('''SELECT *
                            FROM charts
                            WHERE charts.chart_id = :pid''',{"pid":p_chart_id})
            data2 = self.cursor.fetchall()
        #fill the entering date
        self.cursor.execute('''INSERT INTO charts
                            VALUES (?,?,datetime('now'),NULL)
                        ''',(p_chart_id,patient_hcno))
        self.conn.commit()

    def close_chart(self):
        print "Close the patient's chart when he leaves."
        p_hcno = raw_input("The hcno of the leaving patient >")
        #p_edate = datetime('now')
        #fill the leaving date
        self.cursor.execute('''UPDATE charts
                                SET edate = datetime('now')
                                WHERE hcno = :p_h AND edate IS NULL''',{"p_h":p_hcno})
        self.conn.commit()
 



