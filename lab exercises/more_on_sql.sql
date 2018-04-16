-- Products Tables

DROP TABLE IF EXISTS pc;
DROP TABLE IF EXISTS printer;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS laptop;


CREATE TABLE product(
	MAKER    TEXT,
	MODEL INTEGER,
	TYPE  TEXT,
	PRIMARY KEY (MAKER, MODEL)
);

CREATE TABLE pc(
	MODEL INTEGER,
	SPEED INTEGER,
	RAM   INTEGER,
	HD    REAL,
	PRICE INTEGER,
	PRIMARY KEY (MODEL)
);

CREATE TABLE laptop(
	MODEL INTEGER,
	SPEED INTEGER,
	RAM   INTEGER,
	HD    REAL,
	PRICE INTEGER,
	PRIMARY KEY (MODEL)
);

CREATE TABLE printer(
	MODEL INTEGER,
	COLOR TEXT,
	TYPE  TEXT,
	PRICE INTEGER,
	PRIMARY KEY (MODEL)
);



INSERT INTO product VALUES ("A", 1001, "pc");
INSERT INTO product VALUES ("A", 1002, "pc");
INSERT INTO product VALUES ("A", 1003, "pc");
INSERT INTO product VALUES ("A", 2003, "laptop");
INSERT INTO product VALUES ("B", 1004, "pc");
INSERT INTO product VALUES ("B", 2001, "laptop");
INSERT INTO product VALUES ("B", 2002, "laptop");
INSERT INTO product VALUES ("B", 1003, "pc");
INSERT INTO product VALUES ("C", 2001, "laptop");
INSERT INTO product VALUES ("C", 2002, "laptop");
INSERT INTO product VALUES ("C", 2003, "laptop");
INSERT INTO product VALUES ("D", 2002, "laptop");
INSERT INTO product VALUES ("D", 2003, "laptop");
INSERT INTO product VALUES ("D", 2004, "laptop");
INSERT INTO product VALUES ("D", 3004, "printer");
INSERT INTO product VALUES ("E", 2002, "laptop");
INSERT INTO product VALUES ("F", 2002, "laptop");
INSERT INTO product VALUES ("D", 2005, "laptop");
INSERT INTO product VALUES ("D", 3001, "printer");
INSERT INTO product VALUES ("A", 3002, "printer");
INSERT INTO product VALUES ("A", 3003, "printer");
INSERT INTO product VALUES ("A", 3005, "printer");
INSERT INTO product VALUES ("B", 3006, "printer");


INSERT INTO pc VALUES (1001, 133, 16, 1.6, 1595);
INSERT INTO pc VALUES (1002, 120, 16, 1.6, 1399);
INSERT INTO pc VALUES (1003, 166, 24, 2.5, 1899);
INSERT INTO pc VALUES (1004, 166, 32, 2.5, 1999);


INSERT INTO laptop VALUES (2001, 100, 20, 1.1,  1999);
INSERT INTO laptop VALUES (2002, 117, 12, 0.75, 2499);
INSERT INTO laptop VALUES (2003, 117, 32, 1,    3599);
INSERT INTO laptop VALUES (2004, 133, 16, 1.1,  3499);
INSERT INTO laptop VALUES (2005, 166, 16, 4.1,  3599);


INSERT INTO printer VALUES (3001, "true",  "ink-jet", 275);
INSERT INTO printer VALUES (3002, "true",  "ink-jet", 269);
INSERT INTO printer VALUES (3003, "false", "laser",   829);
INSERT INTO printer VALUES (3004, "false", "laser",   879);
INSERT INTO printer VALUES (3005, "true",  "laser",   885);
INSERT INTO printer VALUES (3006, "true",  "laser",   890);





