from django.contrib import admin
from django.utils.html import format_html
from ourguards.models import Ourguards

class OurguardsAdmin(admin.ModelAdmin):
    list_display = ('person','post','img_tag')
    readonly_fields = ('img_tag',)

    def img_tag(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="max-height:100px;" />', obj.img.url)
        return ''
    img_tag.short_description = 'Image'

    fields = ('person','post','img','img_tag')

admin.site.register(Ourguards, OurguardsAdmin)
