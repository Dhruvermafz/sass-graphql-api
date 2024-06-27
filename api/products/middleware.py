from django.utils.deprecation import MiddlewareMixin

class DisableCSRFForGraphQL(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/graphql/':
            setattr(request, '_dont_enforce_csrf_checks', True)
