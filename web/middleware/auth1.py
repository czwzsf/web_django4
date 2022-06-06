from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class login_checking(MiddlewareMixin):
    """利用中间件来验证是否登入了"""

    def process_request(self, request):
        if request.path_info in ["/login/"]:
            return None
        info_dict = request.session.get("info")
        if info_dict:
            return None
        return redirect('/login/')
