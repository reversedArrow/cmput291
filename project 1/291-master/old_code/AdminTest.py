import sqlite3
from Admin import Admin
 
if __name__ == "__main__":
    db_file_path = "./hospital.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    admin00 = Admin('12345', conn, cursor)
    admin01 = Admin('12346', conn, cursor)
    admin02 = Admin('12347', conn, cursor) 
    admin00.admin_menu()