from django.contrib import admin

# Register your models here.
from genius.models import Activity, CaseHistory


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('date', 'place')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(CaseHistory)
