import sqlite3
from AccountManager import AccountManager
 
if __name__ == "__main__":
    db_file_path = "waste_management.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    manager00 = AccountManager(23451, conn, cursor)
    manager01 = AccountManager(23452, conn, cursor) 
    manager00.menu()
