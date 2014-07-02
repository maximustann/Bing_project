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
	ID		varchar(80),
	size_	varchar(80),
	brand	varchar(80),
	retail_price	real,
	cost	real,
	primary key (ID)
);


CREATE TABLE invoice 
(
	invoice_no	varchar(80),
	date_in		date,
	tel			varchar(80),
	name		varchar(80),
	rego		varchar(80),
	money_in	real,
	primary key (invoice_no),
	foreign key (tel) references customer(tel)
);

