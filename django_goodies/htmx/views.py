from django.http import HttpResponse

def js_check(request):
    """
    View to set a cookie indicating that JavaScript is enabled.
    """
    response = HttpResponse("ok")
    response.set_cookie("has_js", "1")
    return response
