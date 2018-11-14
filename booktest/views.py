from django.shortcuts import render
from booktest.models import *
# Create your views here.
def index(request):
    list= BookInfo.books_guanliqi1.filter(heroinfo__hcomment__contains='吧')
    # 模板中数据用的是键  这是上下文管理
    context = {'listlalala':list}
    return  render(request,'booktest/index.html',context)