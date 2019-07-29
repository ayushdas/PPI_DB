from django.db import models

# Create your models here.

class domain_agent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    parent_rule_id = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    rule_structure = models.CharField(max_length = 100)
    ref = models.CharField(max_length = 100)
    rate_constant = models.CharField(max_length = 100)
    kinetic_constant = models.CharField(max_length = 100)
    dimension = models.CharField(max_length = 100)
    estimated = models.CharField(max_length = 100)
    source = models.CharField(max_length = 100)
    model_source = models.CharField(max_length = 100)
    comments = models.CharField(max_length = 100)
    agents = models.CharField(max_length = 100)
    domains = models.CharField(max_length = 100)
    agent_domain_pairs = models.CharField(max_length = 100)
    # domain_id = models.CharField(max_length = 100)
    # agent_id = models.CharField(max_length = 100)

class domain_pairs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    parent_rule_id = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    rule_structure = models.CharField(max_length = 100)
    ref = models.CharField(max_length = 100)
    rate_constant = models.CharField(max_length = 100)
    kinetic_constant = models.CharField(max_length = 100)
    dimension = models.CharField(max_length = 100)
    estimated = models.CharField(max_length = 100)
    source = models.CharField(max_length = 100)
    model_source = models.CharField(max_length = 100)
    comments = models.CharField(max_length = 100)
    agents = models.CharField(max_length = 100)
    domains = models.CharField(max_length = 100)
    agent_domain_pairs = models.CharField(max_length = 100)









