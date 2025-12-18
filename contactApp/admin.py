from django.contrib import admin
from django.utils.html import format_html
from contactApp.models import Contactform, Ourguards

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','phone','message','image_tag','attachment_link','created_at')
    readonly_fields = ('created_at','image_tag','attachment_link')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;" />', obj.image.url)
        return ''
    image_tag.short_description = 'Image'

    def attachment_link(self, obj):
        if obj.attachment:
            return format_html('<a href="{}">{}</a>', obj.attachment.url, obj.attachment.name.split('/')[-1])
        return ''
    attachment_link.short_description = 'Attachment'

    fields = ('fullname','email','phone','message','image','attachment','image_tag','attachment_link','created_at')

class OurguardsAdmin(admin.ModelAdmin):
    list_display = ('person','post','img_tag')
    readonly_fields = ('img_tag',)

    def img_tag(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="max-height:100px;" />', obj.img.url)
        return ''
    img_tag.short_description = 'Image'

    fields = ('person','post','img','img_tag')

# Register the models
admin.site.register(Contactform, ContactAdmin)
admin.site.register(Ourguards, OurguardsAdmin)
