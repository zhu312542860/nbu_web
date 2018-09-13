# coding:utf-8
from django.shortcuts import render
from learn import models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
import os
import json
from models import policy
from django.db.models import Q
 
def index(request):

    return render(request,'index.html')



def job(request):
    policy_data = policy.objects.all()
    tmp_list1 = []
    for i in policy_data:
        tmp_list2 = []
        tmp_list2.append(str(i.policy))
        tmp_list2.append(str(i.policy_clients))
        tmp_list2.append(str(i.policy_stu))
        tmp_list2.append(str(i.policy_pool))
        tmp_list2.append(str(i.policy_type))
        tmp_list2.append(str(i.policy_sched_type))
        tmp_list2.append(str(i.policy_sched_retention))
        tmp_list2.append(str(i.policy_sched_frequency))
        tmp_list2.append(str(i.policy_include))
        tmp_list2.append(str(i.policy_windows))
        tmp_list1.append(tmp_list2)
    return render(request,'home.html',{"data":tmp_list1})

def policy_html(request):
    return render(request,'job.html')

def policy_json(request,method='POST'):
    policy_data = policy.objects.all()
    tmp_list1 = []

    draw = int(request.POST['draw'])
    recordsTotal = policy_data.count()
    recordsFiltered = recordsTotal
    new_search = request.POST['search[value]']

    start = int(request.POST['start'])
    length = int(request.POST['length'])
    print new_search

    if new_search:                
        policy_data = policy.objects.filter(Q(policy= new_search) | Q(policy_clients=new_search) |
                   Q(policy_type=new_search) | Q(policy_stu=new_search))

    datas = policy_data[start:(start+length)]


    for i in datas:
        data = {}
        data['policy'] = i.policy
        data['policy_clients'] = i.policy_clients
        data['policy_stu'] = i.policy_stu
        data['policy_pool'] = i.policy_pool
        data['policy_type'] = i.policy_type
        data['policy_sched_type'] = i.policy_sched_type
        data['policy_sched_retention'] = i.policy_sched_retention
        data['policy_sched_frequency'] = i.policy_sched_frequency
        data['policy_include'] = i.policy_include
        data['policy_windows'] = i.policy_windows
        tmp_list1.append(data)


    result = {
        'draw': draw,
        'recordsTotal': recordsTotal,
        'recordsFiltered': recordsFiltered,
        'data': tmp_list1,
        }

    return HttpResponse(json.dumps(result), content_type="application/json")

def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.message.objects.create(username=username, password=password)
        models.message().save()
    return render_to_response('insert.html')


def list(request):
    people_list = models.message.objects.all()
    c = Context({"people_list": people_list})
    return render_to_response("showuser.html", c)



def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'zsh.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })
