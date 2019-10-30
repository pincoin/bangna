from django.utils.translation import ugettext_lazy as _
from django.views import generic


class MonthlyCalendarListView(generic.TemplateView):
    template_name = 'golf/monthly_calendar_list.html'

    def get_context_data(self, **kwargs):
        context = super(MonthlyCalendarListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Calendar Year {}'.format(self.kwargs['year']))

        return context
