from django.contrib import admin
from django.urls import (
    path, include
)

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('i18n/',
         include('django.conf.urls.i18n')),

    path('accounts/', include('allauth.urls')),

    path('golf/',
         include('golf.urls', namespace='golf')),

    path('',
         HomeView.as_view(), name='home'),
]
