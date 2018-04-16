DROP TABLE IF EXISTS resource;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS provide;



CREATE TABLE resource(

	resource_id INTEGER,
	name TEXT,
	owner  TEXT,
	dir_path TEXT,
	last_modified_date TEXT,
	number_of_available_servers INTEGER,
	PRIMARY KEY (resource_id)

);

CREATE TABLE client(

	client_id TEXT,
	username TEXT,
	email TEXT,
	password TEXT,
	PRIMARY KEY (client_id)

);

CREATE TABLE provide(

	client_id TEXT,
	resource_id INTEGER,
	providing_date DATE,
	FOREIGN KEY(client_id) REFERENCES client(client_id),
    FOREIGN KEY(resource_id) REFERENCES resource(resource_id),
    PRIMARY KEY (client_id, resource_id)
);


INSERT INTO resource VALUES (1,"index.html", "root" ,"/usr/share/local/", "2012",1);
INSERT INTO resource VALUES (2,"data_january_2015.csv", "sysadmin" ,"/usr/bin/", "2015",2);
INSERT INTO resource VALUES (3,"server.py", "root" ,"/srv/", "2016",3);
INSERT INTO resource VALUES (4,"sitemap.html", "user" ,"/home/root/.local/", "2016",5);
INSERT INTO resource VALUES (5,"main.css", "user" ,"/srv/", "2016",1);
INSERT INTO resource VALUES (6,"main.js", "user" ,"/srv/", "2009",2);
INSERT INTO resource VALUES (7,"config.txt", "root" ,"/home/root/docuemnts/configs/", "2016",4);
INSERT INTO resource VALUES (8,"test_module.c", "root" ,"/home/root/Desktop/", "2016",2);
INSERT INTO resource VALUES (9,"my_font.sfd", "sysadmin" ,"/home/sysadmin/.fonts/", "2016",3);
INSERT INTO resource VALUES (10,"my_font.ttf", "user" ,"/home/user/.fonts/", "2016",2);


INSERT INTO client VALUES ('1509101',"saeed.najafi", "saeed.najafi@university.ca" ,"123456");
INSERT INTO client VALUES ('1509102',"sara.farazi", "sara.farazi@university.ca" ,"123456789");
INSERT INTO client VALUES ('1509103',"alex.golrikh", "alex.golrikh@university.ca" ,"1234567890");
INSERT INTO client VALUES ('1509104',"donald.clinton", "donald.clinton@university.ca" ,"9876543210");
INSERT INTO client VALUES ('1509105',"luis.azuro", "luis.azuro@university.ca" ,"147852369");


INSERT INTO provide VALUES ('1509101',2,"2016-11-11");
INSERT INTO provide VALUES ('1509101',3,"2016-10-10");
INSERT INTO provide VALUES ('1509101',4,"2016-10-16");
INSERT INTO provide VALUES ('1509102',1,"2016-10-12");
INSERT INTO provide VALUES ('1509102',2,"2016-09-21");
INSERT INTO provide VALUES ('1509102',3,"2016-09-23");
INSERT INTO provide VALUES ('1509102',6,"2016-10-04");
INSERT INTO provide VALUES ('1509103',6,"2016-09-13");
INSERT INTO provide VALUES ('1509103',7,"2016-11-13");
INSERT INTO provide VALUES ('1509103',8,"2016-10-05");
INSERT INTO provide VALUES ('1509104',8,"2016-09-12");
INSERT INTO provide VALUES ('1509105',9,"2016-11-16");
