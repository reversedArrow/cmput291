# Author: Zhenzhe Xu
# Date: 22/11/2016
# CCID: zhenzhe

import sqlite3
from random import randint
import time
import sys

conn = sqlite3.connect('lab04.db')

def main():
    is_valid = True
    while is_valid:
        print "1.Introduce a new resource"
        print "2.Search resources by name"
        print "3.Provide a resource for a client"
        print "4.Update # of servers"
        print "5.Exit\n"
        choose = raw_input("Choose what you want: ")
        if choose == '1':
            add_resource()
        if choose == '2':
            search_resource()
        if choose == '3':
            add_resource_forclient()
        if choose == '4':
            conn.close()
            sys.exit()

# choose 1
# Introduce a new resource into the app
def add_resource():
    unique = True
    while unique:
        resource_id = str(randint(11,10000))
        if check_unique_id(resource_id):
    		 break
    name = raw_input("Please enter resource name: ")
    owner = raw_input("Please enter the owner of the resource: ")
    dir_path = raw_input("Please enter dir_path: ")
    last_modified_date = raw_input("Please enter the last modified date: ")
    number_of_available_servers = raw_input("Please enter the number of available servers: ")

    try:
        c = conn.cursor()
        c.execute('''INSERT INTO resource VALUES (?, ?, ?, ?, ?, ?)''',
                    (resource_id, name, owner, dir_path, last_modified_date, number_of_available_servers, ))
        conn.commit()
    except sqlite3.Error as e:
        print "Error: " + e.message

def check_unique_id(re_id):
    c = conn.cursor()
    c.execute('''SELECT * FROM resource
                 WHERE resource_id = ?''', (re_id, ))
    row = c.fetchall()
    if not row:
        return True

# Choose 2
# Search resources by name
def search_resource():
    search_name = raw_input("Please enter the name of the resource: ")
    c = conn.cursor()
    c.execute('''SELECT * FROM resource
                 WHERE name = ?''', (search_name, ))
    row = c.fetchall()

    # If there is no searching result:
    if not row:
        print "No result\n"
        return
    print row


# Choose 3
# Provide a resource for a client
def add_resource_forclient():
    
    # select client
    c = conn.cursor()
    c.execute('''SELECT client_id, username FROM client''')
    row = c.fetchall()
	# for i in row:
	# 	print(row[0],row[1])
    # table.add_column("Client id", [i[0] for i in row])
    # table.add_column("Client username", [j[1] for j in row])
    # print table
    c.execute('''alter table client add "providing_date";''')

    cl_id = input("Please enter a client id: ")
    if cl_id not in [i[0] for i in row]:
        print "Client DNE\n"
        return

    # add resource
    c = conn.cursor()
    c.execute('''SELECT resource_id, name, FROM resource''')
    row = c.fetchall()
    table.add_column("Resource id", [i[0] for i in row])
    table.add_column("Resource name", [j[1] for j in row])
    print table

    re_id = raw_input("Please enter a resource id: ")
    if re_id not in [i[0] for i in row]:
        print "Resource DNE"
        return

    if not check_server(re_id):
        print "No more server\n"
        return

    # date
    add_date = time.strftime("%Y-%m-%d %H:%M")
    try:
        c = conn.cursor()
        c.execute('''INSERT INTO provide VALUES (?, ?, ?)''', (cl_id, re_id, add_date, ))
        conn.commit()
        adjust_server_num(re_id)
    except sqlite3.Error as e:
        print "Error: " + e.message

# check the updated # of available servers
def check_server(re_id):
    c = conn.cursor
    c.execute('''SELECT number_of_available_servers FROM resource
                 WHERE resource_id = ?''', (re_id, ))
    row = c.fetchall()
    if row:
        if row[0][0] == 0:
            return False
        else:
            return True

# adjust the server number
def adjust_server_num(re_id):
    c = conn.cursor()
    c.execute('''SELECT * FROM resource
                 WHERE resource_id = ?''', (re_id, ))
    row = c.fetchall()
    num = row[0][5]
    num -= 1
    print num
    print num
    c.execute('''UPDATE resource
                 SET number_of_available_servers = ?
                 WHERE resource_id = ?''', (num, re_id, ))
    conn.commit()


if __name__ == "__main__":
    main()
