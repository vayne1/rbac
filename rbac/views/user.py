from django.shortcuts import redirect,render,HttpResponse
from django.urls import reverse
from rbac import models
from rbac.forms.user import UserModelForm,UpdateUserModelForm,ResetUserModelForm


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_queryset = models.UserInfo.objects.all()

    return render(request,'rbac/user_list.html',{'users':user_queryset})


def user_add(request):
    """
    添加用户
    :param request:
    :return:
    """

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))
    if request.method == 'GET':
        form = UserModelForm()

    # for i in form:
    #     print(i.errors)

    return render(request,'rbac/change.html',{'form':form})


def user_edit(request,pk):
    """
    编辑用户
    :param request:
    :param pk:  用户id
    :return:
    """
    obj = models.UserInfo.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    form = UpdateUserModelForm(instance=obj,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    if request.method == 'GET':
        form = UpdateUserModelForm(instance=obj)
    return render(request,'rbac/change.html',{'form':form})



def user_reset_pwd(request,pk):
    """
    重置密码
    :param request:
    :param pk:
    :return:
    """
    obj = models.UserInfo.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    form = ResetUserModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    if request.method == 'GET':
        form = ResetUserModelForm()
    return render(request, 'rbac/change.html', {'form': form})



def user_del(request,pk):
    """
    删除用户
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:user_list')
    if request.method == 'GET':
        return render(request,'rbac/delete.html',{'cancel':origin_url})
    models.UserInfo.objects.filter(pk=pk).delete()
    return redirect(origin_url)