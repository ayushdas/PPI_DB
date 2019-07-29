from django.shortcuts import render
from ppi.models import domain_agent
from ppi.models import domain_pairs
from django.http import HttpResponse
import ppi.templates

# Create your views here.
def renderAgentNameForm(request):
    # form = agentNameForm()
    # return render(request,'agentName/agentName.html')
    return render(request,'agentName/agentName.html')

def renderDomainNameForm(request):
       return render(request,'domainName/domainName.html')

def getValuesByAgentName(request,agentName='default'):
    context = {}
    context['agentName'] = request.POST.get('agentName', 'default')
    agentName = context['agentName']
    if (agentName == 'default'):
        error =  {'error': 'WARNING: No Valid Results Found! Please enter a valid agent name.'}       
        args = {'posts': error}
        return render(request,'agentName/agentNameError.html',args)
        # return HttpResponse('Please enter an agent name!')
    agentName = '\'' + agentName + '\''
    sql_query = "call GetRulesFromAgentName("+ agentName + ")"
    vals = domain_agent.objects.raw(sql_query)
    args = {'posts': vals}
    lst = []
    for val in vals:
        lst.append((val.id,
        val.name,
        val.parent_rule_id,
        val.description,
        val.rule_structure,
        val.ref,
        val.rate_constant,
        val.kinetic_constant,
        val.dimension,
        val.estimated,
        val.source,
        val.model_source,
        val.comments))
    result = ''
    for val in lst:
        result += str(val)
        result += "  "
    if (len(lst) > 0):
        # return HttpResponse(result) This can be used for debugging based on simple HTML Resposne
        return render(request,'agentName/agentNameRules.html',args)
    else:
        error = {'error': 'WARNING: No Valid Results Found!'}
        args = {'posts': error}
        return render(request,'agentName/agentNameError.html',args)
        # return HttpResponse('No Valid Results Found!') This can be used for debugging based on simple HTML Resposne

def getValuesByDomainNamePair(request,domainName1='default',domainName2='default'):
    context = {}
    context['domainName1'] = request.POST.get('domainName1', 'default')
    context['domainName2'] = request.POST.get('domainName2', 'default')
    domainName1 = context['domainName1']
    domainName2 = context['domainName2']
    if (domainName1 == 'default' or domainName2 == 'default'):
        # return HttpResponse('Please enter both domain names!')
        error = {'error': 'WARNING: Please enter both domain names!'}
        args = {'posts': error}
        return render(request,'domainName/domainNameError.html',args)
    domainName1 = '\'' + domainName1 + '\''
    domainName2 = '\'' + domainName2 + '\''
    domainNames = domainName1 + "," + domainName2
    sql_query = "call GetRulesFromDomainNamesPair("+ domainNames + ")"
    vals = domain_pairs.objects.raw(sql_query)
    args = {'posts': vals}
    lst = []
    for val in vals:
        lst.append((val.id,
        val.name,
        val.parent_rule_id,
        val.description,
        val.rule_structure,
        val.ref,
        val.rate_constant,
        val.kinetic_constant,
        val.dimension,
        val.estimated,
        val.source,
        val.model_source,
        val.comments))
    result = ''
    for val in lst:
        result += str(val)
        result += "  "
    if (len(lst) > 0):
        return render(request,'domainName/domainNameRules.html',args)
    else:
        error = {'error': 'WARNING: No Valid Results Found!'}
        args = {'posts': error}
        return render(request,'domainName/domainNameError.html',args)
        # return HttpResponse('No Valid Results Found!')