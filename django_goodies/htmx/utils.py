def is_htmx(request):
    """
    Check if the request is an HTMX request.
    """
    return request.headers.get("HX-Request") == "true"


def is_js_enabled(request):
    """
    Check if the user has JavaScript enabled based on a cookie.
    """
    return getattr(request, "has_js", False)
