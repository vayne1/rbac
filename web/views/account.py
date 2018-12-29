from django.shortcuts import render,HttpResponse,redirect
from rbac import models
from rbac.service.init_permission import init_permision

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    user = request.POST.get('username')
    pwd = request.POST.get('password')

    current_user = models.UserInfo.objects.filter(name=user,password=pwd).first()


    if not current_user:
        return render(request,'login.html',{'msg':'用户名密码错误'})
    init_permision(current_user, request)
    # for item in permission_queryset:
    #     print(item)
    return redirect('/customer/list/')

