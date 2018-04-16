import sqlite3
from Nurse import Nurse
 
if __name__ == "__main__":
    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    nurse00 = Nurse('12351', conn, cursor)
    nurse00.nurse_menu()