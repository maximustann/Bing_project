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
	date_in		varchar(80),
	tel			varchar(80),
	name		varchar(80),
	rego		varchar(80),
	money_in	varchar(80),
	primary key (invoice_no),
	foreign key (tel) references customer(tel)
);

CREATE TABLE make
(
	name	varchar(80),
	primary key (name)
);

CREATE TABLE model
(
	ID 		integer,
	name	varchar(80),
	make_name varchar(80),
	primary key (ID),
	foreign key (make_name) references make(name)
);
