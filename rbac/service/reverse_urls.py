from django.urls import reverse
from django.http import QueryDict


def memory_url(request,name,*args,**kwargs):
    """
    生成带有源搜索条件的URL
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    basic_url = reverse(name, args=args, kwargs=kwargs)
    query_dict = QueryDict(mutable=True)
    query_dict['_filter'] = request.GET.urlencode()
    return '%s?%s' % (basic_url, query_dict.urlencode())

def memory_reverse(request, name, *args, **kwargs):
    """
    反向生成URl，将url中原来的搜索条件还原
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    url = reverse(name,args=args,kwargs=kwargs)
    origin_params = request.GET.get('_filter')
    if origin_params:
        url = '%s?%s' % (url, origin_params)
    return url

