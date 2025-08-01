from django.contrib import admin
from website.models import contact,Newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
        date_hierarchy = ('created_date')
        list_display = ('Name','email','created_date')
        list_filter = ('email',)
        search_fields = ('Name','message')

admin.site.register(contact,ContactAdmin)
admin.site.register(Newsletter)