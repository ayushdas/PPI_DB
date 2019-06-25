CREATE TABLE rule (
id int, 
name varchar(250),
parent_rule_id int,
description varchar(250),
rule_structure varchar(250),
ref varchar(250),
rate_constant varchar(250),
kinetic_constant varchar(250),
dimension varchar(250),
estimated varchar(250),
source varchar(250), 
model_source varchar(250),
comments varchar(2000),
agents varchar(500),
domains varchar(250),
agent_domain_pairs varchar(250),
PRIMARY KEY (id) 
);