import sqlite3

class check():

    path = 'waste_management.db'

    def __init__(self):
        #database initialization
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = sqlite3.Row
        self.cursor.execute(' PRAGMA foreign_keys = ON; ')
      


    def check_exist_username(self):
        self.cursor.execute('''select login from users''')
        rows = self.cursor.fetchall()
        username = []
        for row in rows:
            username.append(row[0])
        return set(username)

    def check_personnel_id(self):
        self.cursor.execute('''select pid from personnel where pid not in (select user_id from users)''')
        rows = self.cursor.fetchall()
        pid  = []
        for row in rows:
            pid.append(row[0])
        return set(pid)

    def creat_data_for_newuser(self,pid,username,password,role):
        self.cursor.execute('''insert into users values(?,?,?,?)''',(pid,role,username,password))
        self.connection.commit()


    def checkPassword(self,username,password):
        self.cursor.execute('select password from users where login = ?',(username,))
        row = self.cursor.fetchone()
        if row == None or row[0] != password:
            return False
        else:
            return True

    def check_role(self,username,password):
        self.cursor.execute('''select role, password from users where login = ?''',(username,))
        row = self.cursor.fetchone()
        if row[0] =='Dispatcher':
            return row[0]
           
        elif row[0] == 'Account Manager':
            
            return row[0]
        elif row[0] == 'Driver':
            
            return row[0]

        elif row[0] == 'Supervisor':
        
            return row[0]

    def getUser_id(self):
        self.cursor.execute('''select user_id from users''')
        rows = self.cursor.fetchall()
        user_idList = list()
        for row in rows:
            user_idList.append(row["user_id"])
        return set(user_idList)
    def getusername(self):
        self.cursor.execute('''select p.name from personnel p, users u where u.user_id = p.pid''')
        rows = self.cursor.fetchall()
        username = list()
        for row in rows:
            username.append(row["name"])
        return set(username)
    def getdriver_id(self):
        self.cursor.execute('''select d.pid from personnel p, drivers d where d.pid = p.pid''')
        rows = self.cursor.fetchall()
        driver_id = list()
        for row in rows:
            driver_id.append(row["pid"])
        return set(driver_id)