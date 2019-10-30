from django.urls import path

from . import views

app_name = 'golf'

urlpatterns = [
    path('calendar/<int:year>/',
         views.MonthlyCalendarListView.as_view(), name="monthly-calendar-list"),
]
