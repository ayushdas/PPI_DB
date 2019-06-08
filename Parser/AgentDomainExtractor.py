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
            if (len(rule_structure) < 1):
                continue
            print("The rule_id is: ",rule_id)
            rule = rule_structure.split("@")[0]
            rule = rule.replace("->",",").replace("<","")
            agent_domains = rule.split(", ")
            domains = []
            agents = []
            agent_plus_domains = []
            for agent_domain in agent_domains:
                agent = agent_domain.split("(")[0]
                agents.append(agent)
                doms = agent_domain.replace(")","")
                if ('(' in doms):
                    doms = doms.split("(")[1]
                doms = doms.split(",")
                # doms = agent_domain.replace(")","").split("(")[1].split(",")
                # doms = agent_domain.replace(")","").split("(")
                # print(doms)
                agent_plus_domain_string = agent + "("
                for dom in doms:
                    dom = dom.split("[")[0]
                    domains.append(dom)
                    agent_plus_domain_string += dom +","
                agent_plus_domain_string = agent_plus_domain_string[:-1] + ")"
                agent_plus_domains.append(agent_plus_domain_string)
            agents = list(set(agents))
            domains = list(set(domains))
            agent_plus_domains = list(set(agent_plus_domains))
            agents.sort()
            domains.sort()
            agent_plus_domains.sort()
            print(agents)
            print(domains)
            print(agent_plus_domains)
            print()
            # w_sheet.write(i, 13, 'Combo I 3-4 year old')
write_copy.save("agent_seperation_domain.xls")