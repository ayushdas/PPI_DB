DELIMITER //
CREATE PROCEDURE GetRulesFromAgentName(IN agentName TEXT)
BEGIN
SELECT * from rule where id in 
	(SELECT distinct(rule_id) 
	from rule_domain_agent 
	where agent_id in 
		(SELECT id 
			from agent 
			where name = agentName));
END //
DELIMITER ;