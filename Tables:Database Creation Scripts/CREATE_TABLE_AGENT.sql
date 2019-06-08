CREATE TABLE agent (id int UNIQUE NOT NULL AUTO_INCREMENT,
name varchar(200) BINARY,
description varchar(200), 
type varchar(200), 
gene varchar(200), 
NCBI_ID varchar(200),
identifier varchar(400), 
reference_number varchar(200), 
comments varchar(1000),
PRIMARY KEY (name)
);