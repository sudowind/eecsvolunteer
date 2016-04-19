from django.contrib import admin

# Register your models here.
from genius.models import Activity, CaseHistory


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'place')


class CaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'computer_model', 'status')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(CaseHistory, CaseHistoryAdmin)
