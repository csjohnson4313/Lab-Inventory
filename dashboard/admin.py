from django.contrib import admin
from .models import Product
from .models import MarqueeText
# Register your models here.

admin.site.register(Product)
admin.site.register(MarqueeText)

admin.site.site_header = 'AETHR Admin Panel'
admin.site.site_title = 'AETHR Admin Panel'

class MarqueeTextAdmin(admin.ModelAdmin):
    list_display = ('text',)