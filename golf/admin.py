from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class BookingTeeOffInline(admin.TabularInline):
    model = models.BookingTeeOff
    extra = 1
    fields = ('tee_off_time',)
    ordering = ('tee_off_time',)


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('holiday', 'country', 'title')
    list_filter = ('holiday', 'country')
    search_fields = ('title',)
    ordering = ('-holiday',)
    date_hierarchy = 'holiday'


class GolfClubAdmin(admin.ModelAdmin):
    pass


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'gender', 'round_date', 'hole', 'pax',
        'green_fee_pay_on_arrival', 'green_fee_sales',
        'cart_fee_pay_on_arrival', 'cart_fee_sales', 'cart_fee_deducted_from_deposit', 'cart_fee_cost',
        'caddie_fee_pay_on_arrival', 'caddie_fee_cost',
    )
    fieldsets = (
        (_('Booking info'), {
            'fields': (
                'requester', 'round_date', 'hole',
            )
        }),
        (_('Customer info'), {
            'fields': (
                'gender', 'last_name', 'first_name', 'pax', 'memo',
            )
        }),
        (_('Green fee'), {
            'fields': (
                'green_fee_sales', 'green_fee_pay_on_arrival', 'green_fee_cost',
            )
        }),
        (_('Caddie fee'), {
            'fields': (
                'caddie_fee_sales', 'caddie_fee_pay_on_arrival', 'caddie_fee_cost',
            )
        }),
        (_('Cart fee'), {
            'fields': (
                'cart_fee_sales', 'cart_fee_pay_on_arrival', 'cart_fee_deducted_from_deposit', 'cart_fee_cost',
            )
        }),
    )
    inlines = (BookingTeeOffInline,)
    date_hierarchy = 'round_date'
    ordering = ('-round_date', 'created')


admin.site.register(models.Holiday, HolidayAdmin)
admin.site.register(models.GolfClub, GolfClubAdmin)
admin.site.register(models.Booking, BookingAdmin)
