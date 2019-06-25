import xlrd
wb = xlrd.open_workbook('rule_baseV0.2.xlsx')
sheet_list = wb.sheet_names()
s = wb.sheet_by_name(sheet_list[2]) # The Agents Workbook
ctr = 1
for i in range(1,385): # Change Here To Control The Rows To Process (Excel has Indices 1...N but Python has Indices 0..N-1)
    vals= []
    rule_id = s.cell(i,0).value
    if ("R" not in rule_id):
        continue
    for j in range(0,17):
        if (j==1):
            continue
        else:
            if (j==0):
                rule_id = str(s.cell(i,j).value).replace('R','')
                vals.append(rule_id)
            elif (j==3):
                parent_rule_id = str(s.cell(i,j).value)                
                if ('R' in parent_rule_id):
                    parent_rule_id = parent_rule_id.replace('R','')
                    vals.append(parent_rule_id)
                else:
                    vals.append(str(0))
            elif (j==5):
                rule = s.cell(i,j).value.split("@")[0]
                vals.append(str(rule))
            elif (j==8 or j==2):
                rule_name = str(s.cell(i,j).value).replace('\'','')
                vals.append(rule_name)
            else:            
                vals.append(str(s.cell(i,j).value))
    ctr = 0    
    sql = "INSERT INTO RULE VALUES ("
    for val in vals:
        if (ctr == 0):
            val = val.replace('\'','')
            sql += val + ","
        elif (ctr == 2):
            val = val.replace('\'','')
            sql += val + ","
        else: 
            sql += '\'' + val + '\''  + ","
        ctr += 1
    sql = sql[:-1]
    sql += ");"
    print(sql) 