#发现项目中的url
from django.conf import settings
from django.utils.module_loading import import_string
from collections import OrderedDict
from django.urls.conf import URLResolver,URLPattern
import re

def check_url_exclude(url):
    """
    排除一些特定的url
    :param url:
    :return:
    """
    exclude_urls = [
        '/admin/.*',

    ]
    for regex in exclude_urls:
        if re.match(regex,url):
            return True

def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    """
    递归函数
    :param pre_namespace: namespace前缀
    :param pre_url: url前缀
    :param urlpatterns: 路由关系表
    :param url_ordered_dict: 保存路由的有序字典
    :return:
    """
    for item in urlpatterns:
        if isinstance(item,URLPattern):
            if not item.name:
                continue
            if pre_namespace:
                name = '%s:%s' %(pre_namespace,item.name)
            else:
                name = item.name
            url = pre_url + str(item.pattern)
            url = url.replace('^','').replace('$','')
            if check_url_exclude(url):
                continue
            url_ordered_dict[name] = {'name':name,'url':url}

        elif isinstance(item,URLResolver):
            if pre_namespace:
                if item.namespace:
                    namespace = '%s:%s' %(pre_namespace,item.namespace)
                else:
                    namespace = item.namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            recursion_urls(namespace, pre_url+str(item.pattern), item.url_patterns, url_ordered_dict)


def get_all_url_dict():
    """
    递归获取项目中所有的url（必须有name别名）
    :return:
    """
    url_ordered_dict = OrderedDict()
    md = import_string(settings.ROOT_URLCONF)
    recursion_urls(None,'/',md.urlpatterns,url_ordered_dict)
    return url_ordered_dict