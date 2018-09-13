from django.db import models

# Create your models here.


class message(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)


class policy(models.Model):
    md_time = models.CharField(max_length=30)
    policy   = models.CharField(max_length=30)            
    policy_clients = models.CharField(max_length=30)        
    policy_stu  = models.CharField(max_length=30)          
    policy_pool = models.CharField(max_length=30)          
    policy_type = models.CharField(max_length=30)          
    policy_sched_type  = models.CharField(max_length=30)   
    policy_sched_retention = models.CharField(max_length=30)
    policy_sched_frequency = models.CharField(max_length=30)
    policy_include  = models.CharField(max_length=30)      
    policy_windows  = models.CharField(max_length=30)