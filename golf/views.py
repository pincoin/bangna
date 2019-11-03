import calendar

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

    def get_queryset(self):
        queryset = models.Booking.objects \
            .prefetch_related('bookingteeoff_set') \
            .filter(round_date='{}-{}-{}'.format(self.kwargs['year'], self.kwargs['month'], self.kwargs['day'])) \
            .order_by('round_time')

        for booking in queryset:
            booking.cashflow = 0

            if booking.green_fee_pay_on_arrival:
                booking.cashflow += booking.green_fee_sales

            booking.cashflow -= booking.green_fee_cost

            if booking.caddie_fee_pay_on_arrival:
                booking.cashflow += booking.caddie_fee_pay_on_arrival

            booking.cashflow -= booking.caddie_fee_cost

            if booking.cart_fee_pay_on_arrival:
                booking.cashflow += booking.cart_fee_pay_on_arrival

            booking.cashflow -= booking.cart_fee_cost

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DailyReportListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Daily Report - {} {} {}'
                                  .format(self.kwargs['day'],
                                          calendar.month_name[int(self.kwargs['month'])],
                                          self.kwargs['year']))

        return context
