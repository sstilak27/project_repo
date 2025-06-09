from django.contrib import admin

# Register your models here.
from testapp.models import HydJobs,BngJobs,PunneJobs
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydjobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BngJobs,BngJobsAdmin)

class PunnejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(PunneJobs,PunnejobsAdmin)