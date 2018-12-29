from django.shortcuts import redirect,render,HttpResponse
from django.urls import reverse
from rbac import models
from rbac.forms.role import RoleModelForm


def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    role_queryset = models.Role.objects.all()

    return render(request,'rbac/role_list.html',{'roles':role_queryset})


def role_add(request):
    """
    添加角色
    :param request:
    :return:
    """

    form = RoleModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))
    if request.method == 'GET':
        form = RoleModelForm()

    return render(request,'rbac/change.html',{'form':form})


def role_edit(request,pk):
    """
    编辑角色
    :param request:
    :param pk:  角色id
    :return:
    """
    obj = models.Role.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    form = RoleModelForm(instance=obj,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    if request.method == 'GET':
        form = RoleModelForm(instance=obj)
    return render(request,'rbac/change.html',{'form':form})



def role_del(request,pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:role_list')
    if request.method == 'GET':
        return render(request,'rbac/delete.html',{'cancel':origin_url})
    models.Role.objects.filter(pk=pk).delete()
    return redirect(origin_url)