from django.contrib import admin

from core.models import Job


class JobAdmin(admin.ModelAdmin):
    ...


admin.site.register(Job, JobAdmin)
