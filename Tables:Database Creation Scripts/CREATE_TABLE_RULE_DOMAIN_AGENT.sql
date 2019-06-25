CREATE TABLE rule_domain_agent (
rule_id int,
domain_id int, 
agent_id int,
FOREIGN KEY (rule_id) REFERENCES rule(id),
FOREIGN KEY (domain_id) REFERENCES domain(id),
FOREIGN KEY (agent_id) REFERENCES agent(id)
);