CREATE TABLE domain_agent (
domain_id int, 
agent_id int,
FOREIGN KEY (domain_id) REFERENCES domain(id),
FOREIGN KEY (agent_id) REFERENCES agent(id)
);