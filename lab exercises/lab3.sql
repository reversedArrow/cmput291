-- Company Tables:

-- The following commands drop the tables in case you have them
-- from earlier runs. 
-- Note the order we are creating the tables and the order we are removing 
-- them due to the foreign key constraints.

DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS department_locations;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS works_on;
DROP TABLE IF EXISTS dependent;


PRAGMA foreign_keys=OFF;
CREATE TABLE department_locations (
  dnum	 INT, 
  location CHAR(15),
  PRIMARY KEY (dnum,location), 
  FOREIGN KEY (dnum) REFERENCES department(dnum) ON DELETE SET NULL  
  );
INSERT INTO department_locations VALUES(1,'Stafford');
INSERT INTO department_locations VALUES(1,'Edmotnon');
INSERT INTO department_locations VALUES(1,'Toronto');
INSERT INTO department_locations VALUES(2,'Vancouver');
CREATE TABLE project ( 
  pname CHAR(15), 
  pno INT,
  location CHAR(15), 
  dnum INT,
  PRIMARY KEY(pno),
  FOREIGN KEY (dnum) REFERENCES department(dnum)   ON DELETE SET NULL
);
INSERT INTO project VALUES('Project1',1,'Stafford',1);
INSERT INTO project VALUES('Project2',2,'Edmonton',1);
INSERT INTO project VALUES('Project3',3,'Vancouver',2);
INSERT INTO project VALUES('Project4',4,'Stafford',3);
INSERT INTO project VALUES('Project5',5,'Edmonton',1);
CREATE TABLE dependent (
	ssn	CHAR(9),
	depd_name	CHAR(15),
	sex	CHAR,
	relationship	CHAR(15),
	birth_date	DATE,
	PRIMARY KEY(ssn,depd_name),
	FOREIGN KEY(ssn) REFERENCES employee ( ssn ) ON DELETE SET NULL
);
INSERT INTO dependent VALUES('1111','Aada','F','sister','1987-04-06');
INSERT INTO dependent VALUES('1111','Brandon','M','brother','1989-03-16');
INSERT INTO dependent VALUES('2222','Austin','M','cousin','1980-10-10');
INSERT INTO dependent VALUES('3333','Fredy','M','father','1954-01-06');
INSERT INTO dependent VALUES('6666','Ashley','F','sister','1947-02-03');
INSERT INTO dependent VALUES('6666','Boris','M','cousin','1980-12-10');
INSERT INTO dependent VALUES('8888','Pedram','M','brother','1987-05-06');
CREATE TABLE employee (
	ssn	CHAR(9),
	name	CHAR(15),
	bdate	DATE,
	address	VARCHAR(30),
	sex	CHAR,
	salary_per_hour	INTEGER,
	super_ssn	CHAR(9),
	dnum	INT,
	PRIMARY KEY(ssn),
	FOREIGN KEY(super_ssn) REFERENCES employee ( ssn ) ON DELETE SET NULL,
	FOREIGN KEY(dnum) REFERENCES department ( dnum ) ON DELETE SET NULL
);
INSERT INTO employee VALUES('1111','Justine Henderson','1985-08-22','101-23 144 Street','M',27,NULL,1);
INSERT INTO employee VALUES('2222','Abdullah Lang','1980-07-13','12-123 12 Street','M',30,NULL,2);
INSERT INTO employee VALUES('3333','Marcus Cruz','1986-01-05','78-23 23 Ave','M',26,'2222',2);
INSERT INTO employee VALUES('4444','Angela Walker','1990-05-23','132-12 98 Street','F',20,'1111',1);
INSERT INTO employee VALUES('5555','Dixie Hartman','1989-07-22','113 Crest Drive','F',21,NULL,3);
INSERT INTO employee VALUES('6666','Salma Cobb','1992-10-22','87-243 101 Street','F',20,'2222',2);
INSERT INTO employee VALUES('7777','John Garette','1987-11-22','76  Ave','M',23,'1111',1);
INSERT INTO employee VALUES('8888','John L. Krause','1951-08-07','3970 47th Avenue','M',34,NULL,4);
INSERT INTO employee VALUES('9999','Fred S. West','1950-12-05','4569 Albert Street','M',33,NULL,4);
CREATE TABLE works_on (
	ssn	CHAR(9),
	pno	INT,
	hours	NUMERIC,
	PRIMARY KEY(ssn,pno),
	FOREIGN KEY(ssn) REFERENCES employee ( ssn ) ON DELETE SET NULL,
	FOREIGN KEY(pno) REFERENCES project ( pno ) ON DELETE SET NULL
);
INSERT INTO works_on VALUES('1111',1,12);
INSERT INTO works_on VALUES('2222',3,24);
INSERT INTO works_on VALUES('6666',2,18);
INSERT INTO works_on VALUES('7777',1,10);
INSERT INTO works_on VALUES('7777',2,10);
INSERT INTO works_on VALUES('7777',5,10);
INSERT INTO works_on VALUES('8888',5,17);
INSERT INTO works_on VALUES('9999',2,25);
CREATE TABLE department (
	dnum	INT,
	dname	CHAR(10),
	mgr_ssn	CHAR(9),
	mgr_start_date	DATE,
	PRIMARY KEY(dnum),
	FOREIGN KEY(mgr_ssn) REFERENCES employee ( ssn ) ON DELETE SET NULL
);
INSERT INTO department VALUES(1,'Sales Department','1111','2017-03-04');
INSERT INTO department VALUES(2,'Production Department','2222','2017-02-01');
INSERT INTO department VALUES(3,'Assessment Department','5555','2017-05-01');
INSERT INTO department VALUES(4,'Design Department','7777','2013-10-10');
INSERT INTO department VALUES(5,'R&D Department','6666','2012-04-14');
PRAGMA foreign_keys=ON;

