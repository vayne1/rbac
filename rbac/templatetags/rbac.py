from permission import settings
from collections import OrderedDict
from django.template import Library
from rbac.service import reverse_urls


import re
register = Library()
@register.inclusion_tag('rbac/left_menu.html')
def static_menu(request):

    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {'left_menu_list':menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
    创建二级菜单
    :return:
    """
    menu_dict = request.session[settings.MENU_SESSION_KEY]

    # 对字典的key进行排序
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:

            if per['id'] == request.current_selected_permission:
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


@register.inclusion_tag('rbac/url_record.html')
def url_record(request):
    return {'record_list':request.url_record}

@register.filter
def has_permission(request,name):
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True

@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URl
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    return reverse_urls.memory_url(request, name, *args, **kwargs)