DELIMITER //
CREATE PROCEDURE GetRulesFromDomainNamesPair(IN domain1 TEXT, IN domain2 TEXT)
BEGIN
DECLARE domain1_id INT DEFAULT 0;
DECLARE domain2_id INT DEFAULT 0;
SELECT id FROM domain WHERE name = domain1 into domain1_id;
SELECT id FROM domain WHERE name = domain2 into domain2_id;
SELECT * from rule 
WHERE id in
(SELECT DISTINCT rule_id FROM
rule_domain_agent
WHERE 
domain_id = domain1_id
AND
rule_id IN (
SELECT DISTINCT rule_id FROM 
rule_domain_agent
WHERE domain_id = domain2_id
));
END //
DELIMITER ;