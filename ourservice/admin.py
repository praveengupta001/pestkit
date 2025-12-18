from django.contrib import admin

# Register your models here.
from ourservice.models import Service, contactfrom
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title','service_desc','service_read_link')

class ContactFromAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','phone','message')

admin.site.register(Service,ServiceAdmin)
admin.site.register(contactfrom, ContactFromAdmin)

