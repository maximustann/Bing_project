INSERT INTO customer VALUES ("0211071907", "Bobo","4 Norwood Place, Johnsonville, Wellington","xuanshenbo@hotmail.com");
INSERT INTO vehicle VALUES ("AFK240", "Toyota", "Levin", "0211071907", "2014-10-24");
INSERT INTO tyre (size_, brand, retail_price, cost)  VALUES ("175/40 R17", "GREEN_MAX", 120.00, 80.00);
INSERT INTO invoice (date_in, tel, name, rego, money_in) VALUES ("2014-07-02", "0211071907", "Bobo", "AFK240", 280.30);

INSERT INTO customer VALUES ("02188888", "Sxo","4 Krd Place, Johnsonville, Wellington", "sfsfg@hotmail.com");
INSERT INTO vehicle VALUES ("GWC520","Honda", "Levin", "021568631", "2015-01-20");
INSERT INTO tyre (size_, brand, retail_price, cost) VALUES ("175/40 R15", "LINGLONG", 100.00, 80.00);
INSERT INTO invoice (date_in, tel, name, rego, money_in) VALUES ("2014-07-03", "02158412","Sxs", "GWC520",120.30);

INSERT INTO customer VALUES ("02158412", "Sxo","4 Krd Place, Kelburn, Wellington", "sfsfg@gmail.com");
INSERT INTO vehicle VALUES ("EES832", "Mazda", "Demio", "0213237", "2015-01-21");
INSERT INTO tyre (size_, brand, retail_price, cost) VALUES ("175/40 R14", "LINGLONG", 180.00, 90.00);
INSERT INTO invoice (date_in, tel, name, rego, money_in) VALUES ("2014-07-04", "02723567", "Sxo", "EES832" ,30);
INSERT INTO make (name) VALUES ("Toyota");
INSERT INTO model (name, make_name) VALUES ("Levin","Toyota");
INSERT INTO make (name) VALUES ("Honda");
INSERT INTO model (name, make_name) VALUES ("Civic","Honda");

INSERT INTO make (name) VALUES ("BMW");
INSERT INTO model (name, make_name) VALUES ("318i","BMW");

