from django.utils.deprecation import MiddlewareMixin
from .models import tenant


class TenantMiddleware(MiddlewareMixin):

    def process_request(self, request):
        host = request.get_host().split(":")[0]

        try:
            request.tenant = tenant.objects.get(domain=host)
        except tenant.DoesNotExist:
            request.tenant = None
