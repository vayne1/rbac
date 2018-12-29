
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from permission import settings
import re


class RbacMiddleware(MiddlewareMixin):


    def process_request(self,request):

        current_url = request.path_info
        # VALID_URL_LIST = [
        #     '/login/',
        #     '/admin/*',
        # ]

        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url,current_url):
                return None

        # permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return HttpResponse('请登录！')

        flag = False
        url_record = [{'title':'首页','url':'#'}]

        for item in permission_list:
            reg = "^%s$" % permission_list[item]['url']
            if re.match(reg,current_url):
                flag = True
                request.current_selected_permission = permission_list[item]['pid'] or permission_list[item]['id']
                if not permission_list[item]['pid']:
                    url_record.append(
                        {'title':permission_list[item]['title'],'url':permission_list[item]['url'],'class':'active'})
                else:
                    url_record.extend([
                        {'title':permission_list[item]['p_title'],'url':permission_list[item]['p_url']},
                        {'title':permission_list[item]['title'],'url':permission_list[item]['url'],'class':'active'},
                    ])

                request.url_record = url_record     #路径导航
                break
        if not flag:
            return HttpResponse('无权访问')

