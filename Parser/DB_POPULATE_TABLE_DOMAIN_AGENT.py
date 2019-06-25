import xlrd
import sys
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="AYUSHisGR88",
  database="PPI"
)

mycursor = mydb.cursor()
sql = "SELECT * from domain"
mycursor.execute(sql)
domainresult = mycursor.fetchall()    
for result in domainresult:
  agents = result[2].split(",")
  domain_id = result[0]
  for agent in agents:
    sql2 = "SELECT id from agent where name like "
    sql2 += '\'%' + agent + '%\''
    mycursor.execute(sql2)
    agent_id = mycursor.fetchall()
    agent_id = agent_id[0][0]
    sql_command = "INSERT INTO domain_agent values (" + str(domain_id) + "," + str(agent_id) + ");"
    # print(domain_id," ",agent_id)
    print(sql_command)



