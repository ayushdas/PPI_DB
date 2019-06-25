import xlrd
import sys
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="AYUSHisGR88",
  database="PPI"
)
file = open('problematic_agents_domains.txt', 'w')
mycursor = mydb.cursor()
sql = "SELECT COUNT(*) FROM RULE"
mycursor.execute(sql)
n = mycursor.fetchall()[0][0]
for i in range(1,n+1):
    # if (i<192):
    #     continue
    # if (i>192):
    #     break
    sql = "SELECT * FROM RULE WHERE ID = " + str(i)
    mycursor.execute(sql)
    rule = mycursor.fetchall()[0][-1]
    agent_domains = rule.split("|")
    ids = []
    for agent_domain in agent_domains:
        agent = agent_domain.split("(")[0]
        domains = agent_domain.split("(")[1].replace(')','').split(",")
        # print(agent)
        # print(domains)
        sql_agent_id = "SELECT ID FROM AGENT WHERE NAME = " + '\'' + agent + '\''
        mycursor.execute(sql_agent_id)
        agent_results = mycursor.fetchall()
        if (len(agent_results) > 0):
            agent_id = agent_results[0][0]
        else:
            print("-- *** Problem in AGENT_NAME, with rule id ",i," agent is ",agent)
            file.write("-- *** Problem in AGENT_NAME, with rule id "+str(i)+" agent is "+str(agent)+"\n")
            # continue
        # print(agent_id)
        for domain in domains:
            if ('~' not in domain):
                # print(domain)
                sql_domain_id = "SELECT ID FROM DOMAIN WHERE NAME = " + '\'' + domain + '\''
                mycursor.execute(sql_domain_id)
                vals = mycursor.fetchall()
                # print(vals)
                if (len(vals) > 0):              
                    domain_id = vals[0][0]
                    ids.append((i,domain_id,agent_id))
                else:
                    print("-- *** Problem in DOMAIN_NAME, with rule id ",i," where domain is ",domain," and agent is "+agent)
                    file.write("-- *** Problem in DOMAIN_NAME, with rule id " + str(i)+ " where domain is " + domain + " and agent is " + agent+ '\n')
                # print(domain_id)
            else:
                state = domain.split("~")[1]
                domain = domain.split("~")[0]
                sql_domain_id = "SELECT ID FROM DOMAIN WHERE NAME = " + '\'' + domain + '\''
                mycursor.execute(sql_domain_id)
                result_set = mycursor.fetchall()
                if (len(result_set) < 2):
                    if (len(result_set) > 0):              
                        domain_id = result_set[0][0]
                        ids.append((i,domain_id,agent_id))
                    else:
                        print("-- *** Problem in DOMAIN_NAME, with rule id ",i," where domain is ",domain," and agent is ",agent)
                        file.write("-- *** Problem in DOMAIN_NAME, with rule id "+ str(i) +" where domain is "+domain+" and agent is "+agent+'\n')
                    # domain_id = result_set[0][0]
                else:
                    sql_domain_id = "SELECT ID FROM DOMAIN WHERE NAME = " + '\'' + domain + '\'' + 'AND STATES LIKE ' + '\'' + "%" + state + "%" +'\''
                    mycursor.execute(sql_domain_id)
                    result_set = mycursor.fetchall()
                    if (len(result_set) > 0):              
                        domain_id = result_set[0][0]
                        ids.append((i,domain_id,agent_id))
                    else:
                        print("-- *** Problem in DOMAIN_NAME, with rule id ",i," where domain is ",domain," and agent is "+agent)
                        file.write("-- *** Problem in DOMAIN_NAME, with rule id "+ str(i) +" where domain is "+domain+" and agent is "+agent+'\n')
                # print(domain_id)
            # ids.append((i,domain_id,agent_id))
    ids = list(set(ids))
    for id in ids:
        sql_statement = "Insert into rule_domain_agent values (" + str(id[0]) + "," + str(id [1]) + "," + str(id[2]) + ");"
        print(sql_statement)
    print("-- Rule:",i," completed")

