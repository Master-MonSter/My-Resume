from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name','email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)