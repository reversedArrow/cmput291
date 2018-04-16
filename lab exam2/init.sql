DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS passenger;
DROP TABLE IF EXISTS reserve;



CREATE TABLE flight(

	flight_id INTEGER,
	source TEXT,
	destination  TEXT,
	departure_date_time DATE,
	airline_name TEXT,
	current_capacity INTEGER,
	PRIMARY KEY (flight_id)

);

CREATE TABLE passenger(

	passenger_id TEXT,
	name TEXT,
	nationality TEXT,
	gender TEXT,
	PRIMARY KEY (passenger_id)

);




CREATE TABLE reserve(

	ps_id TEXT,
	fl_id INTEGER,
	class TEXT,
	booking_date DATE,
	FOREIGN KEY(ps_id) REFERENCES passenger(passenger_id),
    FOREIGN KEY(fl_id) REFERENCES flight(flight_id), 
    PRIMARY KEY (ps_id,fl_id)
);



INSERT INTO flight VALUES (1,"Toronto", "Edmonton" ,"2016-11-22 20:30:00","Air Canada",1);
INSERT INTO flight VALUES (2,"Edmonton", "Toronto" ,"2016-12-11 20:10:00","Westjet",25);
INSERT INTO flight VALUES (3,"Calgary", "Toronto" ,"2017-01-01 23:00:00","Westjet",51);
INSERT INTO flight VALUES (4,"Vancouver", "Toronto" ,"2017-02-05 15:00:00","Air Canada",12);
INSERT INTO flight VALUES (5,"Montreal", "Toronto" ,"2017-01-13 07:10:00","Westjet",61);
INSERT INTO flight VALUES (6,"Toronto", "Vancouver" ,"2017-03-10 07:30:00","Westjet",4);
INSERT INTO flight VALUES (7,"Edmonton", "Vancouver" ,"2017-04-05 07:10:00","Air Canada",17);
INSERT INTO flight VALUES (8,"Calgary", "Montreal" ,"2017-07-01 13:30:00","Westjet",29);
INSERT INTO flight VALUES (9,"Waterloo", "Edmonton" ,"2017-02-20 12:20:00","Air Canada",5);
INSERT INTO flight VALUES (10,"Ottawa", "Toronto" , "2017-03-21 22:00:00","Westjet",6);



INSERT INTO passenger VALUES ('1509101',"Saeed Najafi", "Russia" ,"Male");
INSERT INTO passenger VALUES ('1509102',"Sara Farazi", "China" ,"Male");
INSERT INTO passenger VALUES ('1509103',"Alex Golrikh", "Canada" ,"Female");
INSERT INTO passenger VALUES ('1509104',"Donald Trump", "USA" ,"Male");
INSERT INTO passenger VALUES ('1509105',"Luis Azuro", "Mexico" ,"Female");

INSERT INTO reserve VALUES ('1509101',2,"ECO","2016-11-11");
INSERT INTO reserve VALUES ('1509101',3,"ECO","2016-10-10");
INSERT INTO reserve VALUES ('1509101',4,"ECO","2016-10-16");
INSERT INTO reserve VALUES ('1509102',1,"BUS","2016-10-12");
INSERT INTO reserve VALUES ('1509102',2,"FIR","2016-09-21");
INSERT INTO reserve VALUES ('1509102',3,"BUS","2016-09-23");
INSERT INTO reserve VALUES ('1509102',6,"ECO","2016-10-04");
INSERT INTO reserve VALUES ('1509103',6,"FIR","2016-09-13");
INSERT INTO reserve VALUES ('1509103',7,"FIR","2016-11-13");
INSERT INTO reserve VALUES ('1509103',8,"BUS","2016-10-05");
INSERT INTO reserve VALUES ('1509104',8,"ECO","2016-09-12");
INSERT INTO reserve VALUES ('1509105',9,"ECO","2016-11-16");
