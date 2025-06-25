class JavaScriptDetectionMiddleware:
    """
    Middleware to detect if the user has JavaScript enabled by checking a cookie.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.has_js = request.COOKIES.get("has_js") == "1"
        return self.get_response(request)


class HTMXMiddleware:
    """
    Middleware to detect if the request is an HTMX request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.is_htmx = request.headers.get("HX-Request") == "true"
        return self.get_response(request)
