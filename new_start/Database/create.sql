CREATE TABLE customer
(
	tel 	varchar(80),
	name 	varchar(80),
	Address	varchar(256),
	Email	varchar(256),
	primary key (tel)
);

CREATE TABLE vehicle
(
	rego	varchar(80),
	make	varchar(80),
	model	varchar(80),
	tel		varchar(80),
	expire_date	date,
	primary key (rego, tel),
	foreign key (tel) references customer(tel)
);


CREATE TABLE tyre
(
	ID		integer,
	size_	varchar(80),
	brand	varchar(80),
	retail_price	real,
	cost	real,
	primary key (ID)
);


CREATE TABLE invoice 
(
	invoice_no	integer,
	date_in		date,
	tel			varchar(80),
	name		varchar(80),
	rego		varchar(80),
	money_in	real,
	amount_paid real,
	amount_due	real,
	note		varchar(1024),
	service		varchar(1024),
	labour		varchar(1024),
	model		varchar(1024),
	primary key (invoice_no),
	foreign key (tel) references customer(tel)
);

CREATE TABLE items
(
	invoice_no integer,
	des varchar(1024),
	price	real,
	qty		real,
	unit	varchar(80),
	amount	real,
	amount_gst	real
);

CREATE TABLE make
(
	ID		integer,
	name	varchar(80),
	primary key (ID)
);

CREATE TABLE model
(
	ID 		integer,
	name	varchar(80),
	make_name varchar(80),
	primary key (ID),
	foreign key (make_name) references make(name)
);
