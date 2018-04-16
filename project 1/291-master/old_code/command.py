import sqlite3, hashlib
from Nurse import Nurse
from Doctor import Doctor
from Admin import Admin


def login(cursor):
    login_choice = int(raw_input('''Type integer of desired tasks
                              1. Log in\n
                              2. Shut down\n'''))

    if login_choice == 1:
        indicator = True
    else:
        return
    while indicator:

        username = raw_input("Input username >")
        password = hashlib.sha224(raw_input("Input password >")).hexdigest()

        cursor.execute('''
                        SELECT role
                        FROM staff
                        WHERE login = ?
                        AND password = ?;
                       ''', (username, password, ))

        result = cursor.fetchall()

        if not result:
            print "Invalid login"
        else:
            break

    return result[0][0]

if __name__ == "__main__":

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    username = ""
    role = login(cursor)

    if role == 'D':
        print "You are a doctor"
        doctor = Doctor(username, conn, cursor)
        doctor.doctor_menu()
    elif role == 'N':
        print "You are a nurse"
        nurse = Nurse(username, conn, cursor)
        nurse.nurse_menu()
    elif role == 'A':
        print "You are an admin"
        admin = Admin(username, conn, cursor)
        admin.admin_menu()
