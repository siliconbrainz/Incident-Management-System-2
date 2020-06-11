from django.contrib import admin
from CustomerData.models import SalesData
from CustomerData.models import CSR,CustomerTrack


class SalesDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rcNo', 'model')
    search_fields = ('name', 'rcNo', 'model')


admin.site.register(SalesData, SalesDataAdmin)
admin.site.register(CSR)
admin.site.register(CustomerTrack)
