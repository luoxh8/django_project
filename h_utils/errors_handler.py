from h_utils.response_extra import err_base_server, err_sys_api_not_found


def error404(request, exception, template_name=''):
    return err_sys_api_not_found()


def error500(request, exception, template_name=''):
    return err_base_server()
