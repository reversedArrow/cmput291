import sqlite3
from Dirvers import Driver

if __name__ == "__main__":

    db_file_path = "./waste_management.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    driver = Driver(33250, conn, cursor)
	driver.driver_menu()