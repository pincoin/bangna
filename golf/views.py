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
            .all() \
            .order_by('bookingteeoff__tee_off_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DailyReportListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Daily Report - {} {} {}'
                                  .format(self.kwargs['day'],
                                          calendar.month_name[int(self.kwargs['month'])],
                                          self.kwargs['year']))

        return context
