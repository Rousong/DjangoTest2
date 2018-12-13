from django.shortcuts import render
from booktest.models import *
from django.http import HttpResponse,JsonResponse
from django.core import serializers
# Create your views here.
def index(request):
    list= BookInfo.books_guanliqi1.filter(heroinfo__hcomment__contains='吧')
    # 模板中数据用的是键  这是上下文管理
    context = {'listlalala':list}
    return  render(request,'booktest/index.html',context)


#省市区选择
def area(request):
    return render(request,'booktest/area.html')

def pro(request):

    data=AreaInfo.objects.filter(parea_id=0)

    #print(data)
    list =[]
    for area in data:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})


def city(request,id):
    citylist=AreaInfo.objects.filter(parea__id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})