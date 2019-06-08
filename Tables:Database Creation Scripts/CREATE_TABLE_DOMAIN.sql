CREATE TABLE domain (id int UNIQUE NOT NULL AUTO_INCREMENT,
name varchar(200) BINARY,
agent_name varchar(200) REFERENCES agent,
type varchar(200),
PRIMARY KEY (name)
);