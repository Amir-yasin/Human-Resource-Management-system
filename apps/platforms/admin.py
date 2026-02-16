from django.contrib import admin
from apps.tenants.models import tenant
from apps.accounts.models import user

admin.site.register(tenant)
admin.site.register(user)
