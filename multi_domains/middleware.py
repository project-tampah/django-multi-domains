"""
A small middleware to map domains with specific urlconf.
As a fallback, `ROOT_URLCONF` is still valid.
"""
from django.conf import settings


class MultiDomainsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # get attribute from settings object
        domains = getattr(settings, "MULTI_DOMAINS", None)

        # map the host to the correct urlconf if the settings have been set
        if domains:
            host = request.get_host()
            request.urlconf = domains.get(host)

        return self.get_response(request)
