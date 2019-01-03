from permission import settings

def init_permision(current_user, request):
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                                      'permissions__title',
                                                                                      'permissions__url',
                                                                                      'permissions__name',
                                                                                      'permissions__pid_id',
                                                                                      'permissions__pid__title',
                                                                                      'permissions__pid__url',
                                                                                      'permissions__menu_id',
                                                                                      'permissions__menu__title',
                                                                                      'permissions__menu__icon',
                                                                                      ).distinct()

    permission_dict = {}

    menu_dict = {}

    for item in permission_queryset:
        permission_dict[item['permissions__name']] = {
                'id':item['permissions__id'],
                'url':item['permissions__url'],
                'title':item['permissions__title'],
                'pid':item['permissions__pid_id'],
                'p_title':item['permissions__pid__title'],
                'p_url':item['permissions__pid__url'],
            }

        #左侧菜单
        menu_id = item['permissions__menu_id']
        if not menu_id:
            continue
        node = {'id':item['permissions__id'],'title': item['permissions__title'], 'url': item['permissions__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }
    # request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict