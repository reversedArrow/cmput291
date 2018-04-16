import sqlite3
from Drivers import Driver

if __name__ == "__main__":

    db_file_path = "waste_management.db"
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    driver00 = Driver(33252, conn, cursor)
    driver01 = Driver(33253, conn, cursor)
    driver02 = Driver(33258, conn, cursor)
    driver00.driver_menu()
