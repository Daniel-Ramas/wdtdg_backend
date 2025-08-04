import re
from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware


class CsrfExemptMiddleware:
    """
    Middleware to exempt API endpoints from CSRF protection.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.csrf_exempt_urls = getattr(settings, 'CSRF_EXEMPT_URLS', [])
        self.csrf_exempt_patterns = [re.compile(pattern) for pattern in self.csrf_exempt_urls]

    def __call__(self, request):
        # Check if the request path matches any CSRF exempt patterns
        for pattern in self.csrf_exempt_patterns:
            if pattern.match(request.path):
                setattr(request, '_dont_enforce_csrf_checks', True)
                break
        
        response = self.get_response(request)
        return response 