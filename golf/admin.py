from django.contrib import admin

from . import models


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('holiday', 'country', 'title')
    list_filter = ('holiday', 'country')
    search_fields = ('title',)
    ordering = ('-holiday',)
    date_hierarchy = 'holiday'


class GolfClubAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Holiday, HolidayAdmin)
admin.site.register(models.GolfClub, GolfClubAdmin)
