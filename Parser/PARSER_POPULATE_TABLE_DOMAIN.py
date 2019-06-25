import xlrd

# Open the file
wb = xlrd.open_workbook('rule_baseV0.2.xlsx')

# Get the list of the sheets name
sheet_list = wb.sheet_names()


# Select one sheet and get its size
s = wb.sheet_by_name(sheet_list[1])
# print(s.nrows, s.ncols)


ctr = 1
domains = []
for i in range(1,67): # 68 is the last row in the excel sheet for Agents
    domain_set = []
    agent_and_domains = []
    agent_and_domains = s.cell(i,0).value.replace(')','').split('(')
    if (len(agent_and_domains) > 1):
        domain_set = agent_and_domains[1].split(',')
        domain_set = [domain.strip() for domain in domain_set]
        for domain in domain_set:
            domains.append(domain)
domains = list(set(domains))
# print(domains) ### All the domains obtained at this point

domains_dict = {domain:[] for domain in domains}
# for key, value in domains_dict.items() :
#     print (key, value)

for i in range(1,67): # 68 is the last row in the excel sheet for Agents
    agent_and_domains = s.cell(i,0).value.replace(')','').split('(')
    if (len(agent_and_domains) > 1):
        agent = agent_and_domains[0]
        domain_set = agent_and_domains[1].split(',')
        domain_set = [domain.strip() for domain in domain_set]
        for domain in domain_set:
            domains_dict[domain].append(agent)
        # print(domain,' ',domain_set)
# print('#########')
ctr = 0
for domain, agents in domains_dict.items() :
    ctr += 1
    seperator = ','
    agents_string = '\'' + seperator.join(agents) + '\''
    dt = domain
    state = "none"
    if "~" in domain:
        doms = domain.split("~")
        domain = doms[0]
        if (len (doms) > 1) :
            state = doms[1]
        else:
            state = "none"
    if "{" in domain:
        doms = domain.split("{")
        domain = doms[0]
        if (len (doms) > 1) :
            state = doms[1]
        else:
            state = "none"
    domain = '\'' + domain + '\''
    string = "Insert into domain values ("+str(ctr)+","
    type_of_domain = '\'' + "none" + '\''
    state = '\'' + state + '\''
    string += domain + "," + agents_string + "," + type_of_domain + "," + state + ");"
    # print (domain,agents_string)
    # print(dt," ",domain," ",state,)
    print(string)
    



