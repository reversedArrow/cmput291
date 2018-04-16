import sqlite3
import warnings
from Doctor import Doctor

if __name__ == "__main__":
    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    doctor00 = Doctor('12348', conn, cursor)
    doctor01 = Doctor('12349', conn, cursor)
    doctor02 = Doctor('12350', conn, cursor)

    doctor00.doctor_menu()

