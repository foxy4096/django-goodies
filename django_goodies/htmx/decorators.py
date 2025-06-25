from django.http import HttpResponseBadRequest
from .utils import is_htmx


def htmx_only(view_func):
    """
    Decorator to ensure that a view only processes HTMX requests.
    If the request is not an HTMX request, it returns a 400 Bad Request response
    with a message indicating that the endpoint only accepts HTMX requests.
    """

    def _wrapped(request, *args, **kwargs):
        if not is_htmx(request):
            return HttpResponseBadRequest("This endpoint only accepts HTMX requests.")
        return view_func(request, *args, **kwargs)

    return _wrapped
