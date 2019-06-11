import xlrd
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
wb = xlrd.open_workbook('rule_baseV0.2.xlsx')
sheet_list = wb.sheet_names()
s = wb.sheet_by_name(sheet_list[2])
rb = open_workbook("rule_baseV0.2.xlsx")
r_sheet = rb.sheet_by_index(0) 
write_copy = copy(rb) 
w_sheet = write_copy.get_sheet(2) 
for i in range(1,385): # Change Here To Control The Rows To Process (Excel has Indices 1...N but Python has Indices 0..N-1)
            rule_structure = s.cell(i,5).value
            rule_id = s.cell(i,0).value
            if (len(rule_structure) < 1 or not("@" in rule_structure)):
                continue
            # print("The rule_id is: ",rule_id)
            kineticConstant = rule_structure.split("@")[1]         
            w_sheet.write(i, 16, kineticConstant)
            # print(kineticConstant)
write_copy.save("kinetic_constants.xls")