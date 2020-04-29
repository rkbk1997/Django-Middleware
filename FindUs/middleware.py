from django.shortcuts import HttpResponseRedirect
from django.urls import resolve
def login_register_middleware(get_response):
    def middleware(request):
        url_name=resolve(request.path_info).url_name
        if (url_name=='login' or url_name=='reg') and request.user.is_authenticated:
            response=HttpResponseRedirect('index') 
        else:
            response=get_response(request)
        return response
    return middleware