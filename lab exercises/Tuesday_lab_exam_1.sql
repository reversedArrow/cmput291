DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS take;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS course_location;


CREATE TABLE course(

	course_id INTEGER,
	title TEXT,
	teacher  TEXT,
	text_book TEXT,
	type Text,
	PRIMARY KEY (course_id)

);

CREATE TABLE student(

	student_id INTEGER,
	name TEXT,
	major TEXT,
	gender TEXT,
	PRIMARY KEY (student_id)

);

CREATE TABLE take(

	st_id INTEGER,
	co_id INTEGER,
	semester TEXT,
	FOREIGN KEY(st_id) REFERENCES student(student_id),
    FOREIGN KEY(co_id) REFERENCES course(course_id), 
    PRIMARY KEY (st_id, co_id, semester)
);

CREATE TABLE department(
	department_name TEXT,
	dep_address TEXT,
	PRIMARY KEY (department_name)
);

CREATE TABLE course_location(

	co_id INTEGER,
	dep_id INTEGER,
	FOREIGN KEY(co_id) REFERENCES course(course_id),
    FOREIGN KEY(dep_id) REFERENCES department(department_name), 
    PRIMARY KEY (co_id, dep_id)
);

INSERT INTO course VALUES (1,"Introduction to Algorithms", "Thomas Cormen" ,"Algorithms and Data Structures", "Undergrad");
INSERT INTO course VALUES (2,"Introduction to Programming", "Andrew Tanenbaum" ,"Programming for Beginners", "Undergrad");
INSERT INTO course VALUES (3,"Introduction to Operating Systems", "Abraham Silberschatz" ,"Operating Systems", "Undergrad");
INSERT INTO course VALUES (4,"Software Engineering", "Roger Pressman" ,"UML Distilted", "Grad");
INSERT INTO course VALUES (5,"How to Program", "Saeed Najafi" ,"Computing Science for Beginners", "Undergrad");
INSERT INTO course VALUES (6,"The Personal MBA", "Josh Kaufman" ,"Personal Business", "Grad");
INSERT INTO course VALUES (7,"Programming Languages", "Benjamin Graham" ,"All about PL", "Grad");
INSERT INTO course VALUES (8,"How to Win at the Sport of Business", "Mark Cuban" ,"Win the Business Game", "Grad");
INSERT INTO course VALUES (9,"Advanced Programming", "Tom Bingham" ,"Advanced Programming in JAVA", "Undergrad");
INSERT INTO course VALUES (10,"Introduction to Statistics", "Nicholas McBride" ,"Statistics and Random Variables", "Undergrad");


INSERT INTO student VALUES (1,"John Snow", "CS" ,"M");
INSERT INTO student VALUES (2,"Harry Potter", "CS" ,"M");
INSERT INTO student VALUES (3,"Hermoine Granger", "BUS" ,"F");
INSERT INTO student VALUES (4,"Ygritte", "BUS" ,"F");
INSERT INTO student VALUES (5,"Arya Stark", "LAW" ,"F");

INSERT INTO take VALUES (1,1,"Fall 2012");
INSERT INTO take VALUES (1,2,"Spring 2016");
INSERT INTO take VALUES (1,3,"Fall 2016");
INSERT INTO take VALUES (1,4,"Winter 2016");
INSERT INTO take VALUES (2,1,"Summer 2016");
INSERT INTO take VALUES (2,2,"Fall 2015");
INSERT INTO take VALUES (2,3,"Winter 2015");
INSERT INTO take VALUES (2,1,"Fall 2016");
INSERT INTO take VALUES (2,6,"Spring 2016");
INSERT INTO take VALUES (3,6,"Fall 2014");
INSERT INTO take VALUES (3,7,"Spring 2015");
INSERT INTO take VALUES (3,8,"Winter 2015");
INSERT INTO take VALUES (3,6,"Fall 2011");
INSERT INTO take VALUES (4,5,"Spring 2013");
INSERT INTO take VALUES (4,8,"Spring 2013");
INSERT INTO take VALUES (5,9,"Fall 2015");


INSERT INTO department VALUES ("ETLC","Edmonton, UoA, Engineering Quad");
INSERT INTO department VALUES ("CAB","Edmonton, UoA, Central Academic Building");
INSERT INTO department VALUES ("SAB","Edmonton, UoA, South Academic Building");


INSERT INTO course_location VALUES (1,"ETLC");
INSERT INTO course_location VALUES (2,"ETLC");
INSERT INTO course_location VALUES (3,"ETLC");
INSERT INTO course_location VALUES (4,"ETLC");
INSERT INTO course_location VALUES (5,"ETLC");
INSERT INTO course_location VALUES (6,"ETLC");
INSERT INTO course_location VALUES (7,"ETLC");
INSERT INTO course_location VALUES (8,"ETLC");


INSERT INTO course_location VALUES (1,"SAB");
INSERT INTO course_location VALUES (2,"SAB");
INSERT INTO course_location VALUES (4,"SAB");
INSERT INTO course_location VALUES (6,"SAB");
INSERT INTO course_location VALUES (7,"SAB");
INSERT INTO course_location VALUES (8,"SAB");
INSERT INTO course_location VALUES (9,"SAB");
INSERT INTO course_location VALUES (10,"CAB");
