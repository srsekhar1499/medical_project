from django.contrib import admin
from .models import HealthReport, Audit


class HealthReportAdmin(admin.ModelAdmin):
    model = HealthReport
    list_display = ['user', 'hb', 'bp', 'dpf', 'sleep_time']


class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ['user', 'weight']


admin.site.register(HealthReport, HealthReportAdmin)

admin.site.register(Audit, AuditAdmin)

