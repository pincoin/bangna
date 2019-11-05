import calendar
from decimal import Decimal

from django.utils.translation import ugettext_lazy as _
from django.views import generic

from . import models


class MonthlyCalendarListView(generic.TemplateView):
    template_name = 'golf/monthly_calendar_list.html'

    def get_context_data(self, **kwargs):
        context = super(MonthlyCalendarListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Calendar Year {}'.format(self.kwargs['year']))

        return context


class MonthlyReportListView(generic.TemplateView):
    context_object_name = 'booking_list'
    template_name = 'golf/monthly_report.html'

    def get_context_data(self, **kwargs):
        context = super(MonthlyReportListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Monthly Report - {} {}'
                                  .format(calendar.month_name[self.kwargs['month']], self.kwargs['year']))

        return context


class DailyReportListView(generic.ListView):
    template_name = 'golf/daily_report.html'

    total_pax = Decimal('0')
    total_green_fee = Decimal('0')
    total_caddie_fee = Decimal('0')
    total_cart_fee = Decimal('0')
    total_cart = Decimal('0')
    total_cashflow = Decimal('0')

    def get_queryset(self):
        queryset = models.Booking.objects \
            .prefetch_related('bookingteeoff_set') \
            .filter(round_date='{}-{}-{}'.format(self.kwargs['year'], self.kwargs['month'], self.kwargs['day'])) \
            .order_by('round_time')

        for booking in queryset:
            self.total_pax += booking.pax

            self.total_green_fee += booking.green_fee_sales

            self.total_green_fee -= booking.green_fee_cost

            self.total_caddie_fee += booking.caddie_fee_sales

            self.total_caddie_fee -= booking.caddie_fee_cost

            self.total_cart_fee += booking.cart_fee_sales

            self.total_cart_fee -= booking.cart_fee_cost

            self.total_cart += booking.cart_fee_deducted_from_deposit

            self.total_cashflow += booking.cashflow

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DailyReportListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Daily Report - {} {} {}'
                                  .format(self.kwargs['day'],
                                          calendar.month_name[int(self.kwargs['month'])],
                                          self.kwargs['year']))

        context['total_pax'] = self.total_pax
        context['total_green_fee'] = self.total_green_fee
        context['total_caddie_fee'] = self.total_caddie_fee
        context['total_cart_fee'] = self.total_cart_fee
        context['total_cart'] = self.total_cart
        context['total_cashflow'] = self.total_cashflow

        return context
