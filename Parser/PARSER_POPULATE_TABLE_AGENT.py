import xlrd
wb = xlrd.open_workbook('rule_baseV0.2.xlsx')
sheet_list = wb.sheet_names()
s = wb.sheet_by_name(sheet_list[1]) # The Agents Workbook
ctr = 1
for i in range(1,67): # Change Here To Control The Rows To Process (Excel has Indices 1...N but Python has Indices 0..N-1)
    vals= []
    for j in range(0,8):
        if (j==0):
            agent_name = s.cell(i,j).value.split('(')[0]
            vals.append(agent_name)
        else:            
            vals.append(s.cell(i,j).value)
    string = "Insert into agent values("+str(ctr)+","
    for j in range(len(vals)):               
        string += '\''
        string += str(vals[j])
        string += '\''
        if (j!=(len(vals)-1)):
            string += ","
    string += ");"
    ctr += 1
    print(string)