import sqlite3
from Dispatchers import Dispatcher
 
if __name__ == "__main__":
    db_file_path = "waste_management.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    dispatcher00 = Dispatcher('33006', conn, cursor)
    dispatcher01 = Dispatcher('23453', conn, cursor)
    dispatcher00.dispatcher_menu()
