import sqlite3

connection = None
cursor = None

def connect(path):
    global connection, cursor
    
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    
    return

def question1():
    global connection, cursor
    
    sid = imput("Enter student id: ")
    cursor.execute("select studentname fromstudents where studentid = ?",(sid))
    row = cursor.fetchall()
    
    print("student name: ",row[0][0])
    
    cursor.execute("select c.coursename, p.department from enroll e, course c, professor p where e.studentid = ? and e.courseid = c.courseid and c.professorid = p.professorid",(sid))
    
    row = cursor.fetchall()
    
    for i in row:
        print("course name: ",i[0],"department: ",i[1])
        
    row = cursor.fetchall()
    
    return


def GPA(grade):
    global connection, cursor
    
    if (grade == "A"):
        return 4
    elif(grade == "B"):
        return 3
    elif(grade == "C"):
        return 2
    elif(grade == "D"):
        return 1
    return 0




def question2():
    cursor.execute("delete from selectedstudents; ")
    value = float(input("min gpa: "))
    cursor.execute("select s.student, s.studentname,s.program,avg(gpa(e.grade)) from student s, enroll e where s.studentid = e.studentid group by s.studentid;")
    row = cursor.fetchall()
    for i in row:
        if i[3]>value:
            cursor.execute("insert into selectedstudents values(?,?,?);",(i[0],i[1],i[2]))
    connection.commit()
    return 


def main():
    global connection, cursor
    
    path = "./data.db"
    connect(path)
    connection.create_function('GPA',1,GPA)
    select = input("which question: ")
    if select == 'q1':
        question1()
    elif select == 'q2':
        question2()
    else:
        print("please choose again!")
        return
    connection.commit()
    connection.close()
    
    return

if __name__ == "__main__":
    main()
    