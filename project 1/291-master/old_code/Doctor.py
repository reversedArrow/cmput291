import sqlite3
import warnings


class Doctor:
    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    def __init__(self, staff_id, conn, cursor):
        self.staff_id = staff_id
        self.conn = conn
        self.cursor = cursor

    def doctor_menu(self):
        while True:
            choice = int(raw_input('''
                                    Type integer of desired task
                                    1. list all charts
                                    2. add an entry for symptoms
                                    3. add an entry for diagnosis
                                    4. add an entry for medications
                                    5. log out
                                    '''))

            if choice == 1:
                self.list_chart()
            elif choice == 2:
                self.add_symp()
            elif choice == 3:
                self.add_diag()
            elif choice == 4:
                self.add_medi()
            elif choice == 5:
                return

    # 1. For a given patient, list all charts in the system ordered by adate (indicating also whether they are closed or
    # open). The user should be given the option to select a chart. Once a chart is selected, all entries (symptoms,
    # diagnoses, and medications) associated with that chart must be listed, and the result must be ordered by the date
    # of the entries.
    # http://stackoverflow.com/questions/2396889/how-to-select-true-false-based-on-column-value
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



    # 3. For a given patient and an open chart of the patient add an entry for diagnosis. The date ddate should be set
    # to the current date and time.
    def add_diag(self):
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        hcno = raw_input("To add an entry for diagnosis, enter a patient's hcno: ")
        chart_id_op = raw_input("Also enter the chart_id of an open chart of the patient: ")
        diag2add = raw_input("Enter the diagnosis of this entry: ")

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
                               insert into diagnoses
                               values ('%s', %s, %s, datetime('now'), '%s')
                               ''' % (hcno, chart_id_op, self.staff_id, diag2add))
        self.conn.commit()

    # 4. For a given patient and an open chart of the patient add an entry for medications. The date mdate should be set
    # to the current date and time. Additional checks should be performed before adding the entry:
    # (1) if the prescribed amount for the patient is larger than the recommended amount sug_amount for that drug and
    # the patient's age group, a warning should be issued that contains the information about recommended amount for a
    # patient for that age
    # group, and the doctor should be given the choice to confirm his prescription or to change the amount.
    # (2) If the patient could be allergic to the prescribed drug drug_name, a warning should be issued that contains
    # the information about the reported allergy; the warning should display the name of the drug that the patient
    # reported being allergic to, and, if that is not directly drug_name, the name of the drug D should be displayed,
    # which the patient reported being allergic to and from which it can be "inferred" that the patient may also be
    # allergic to drug_name.
    # http://stackoverflow.com/questions/3891804/how-to-raise-a-warning-in-python-without-stopping-interrupting-the-program
    # http://stackoverflow.com/questions/3289601/null-object-in-python
    def add_medi(self):
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        proper_amount = True
        not_allergic = True

        hcno = raw_input("To add an entry for medications, enter a patient's hcno: ")
        chart_id_op = raw_input("Also enter the chart_id of an open chart of the patient: ")
        drug2add = raw_input("Enter the drug_name of this entry: ")
        amount2add = int(raw_input("Enter the prescribed amount of this medication: "))
        start_med = raw_input("Enter the start date: ")
        end_med = raw_input("Enter the end date: ")

        # if prescribed amount is larger than sug_amount for that drug and the patient's age group
        self.cursor.execute('''
                              select do.sug_amount, pa.age_group
                              from dosage do, patients pa, drugs dr
                              where pa.hcno = :hcno
                                and pa.age_group = do.age_group
                                and dr.drug_name = :drug2add
                                and do.drug_name = dr.drug_name
                              ''', {"hcno": hcno, "drug2add": drug2add})
        row = self.cursor.fetchone()
        if row is not None:
            if amount2add > row[0]:
                proper_amount = False
                warnings.warn("Recommended amount is %d for a patient of age group %s" % (row[0], row[1]))

        # if patient is allergic to the prescribed drug drug_name
        self.cursor.execute('''
                              select ral.drug_name, ial.alg
                              from reportedallergies ral, inferredallergies ial, patients pa, drugs dr
                              where pa.hcno = :hcno
                                and pa.hcno = ral.hcno
                                and dr.drug_name = :drug2add
                                and dr.drug_name = ral.drug_name
                                and dr.drug_name = ial.canbe_alg
                              ''', {"hcno": hcno, "drug2add": drug2add})
        row = self.cursor.fetchone()
        if row is not None:
            if row[0] is not None:
                not_allergic = False
                warnings.warn("The drug that the patient reported being allergic to is %s " % row[0])
            if row[1] is not None:
                not_allergic = False
                warnings.warn("The drug that the patient reported being allergic to is %s , and from which it can"
                              "be 'inferred' that the patient may also be allergic to %s"
                              % (row[1], row[0]))

        if proper_amount and not_allergic:
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
                                   insert into medications
                                   values (?, ?, ?, datetime('now'), ?, ?, ?, ?)
                                   ''', (hcno, chart_id_op, self.staff_id, start_med, end_med, amount2add, drug2add))
            self.conn.commit()
