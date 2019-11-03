from django.urls import path

from . import views

app_name = 'golf'

urlpatterns = [
    path('calendar/<int:year>/',
         views.MonthlyCalendarListView.as_view(), name="monthly-calendar-list"),

    path('report/<int:year>/<int:month>/',
         views.MonthlyReportListView.as_view(), name="monthly-calendar-list"),

    path('report/<int:year>/<int:month>/<int:day>/',
         views.DailyReportListView.as_view(), name="monthly-calendar-list"),
]
