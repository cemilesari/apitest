# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

from .views import CurrenciesList
app_name = 'API'

urlpatterns = [
    path('d/', view=login_required(CurrenciesList.as_view()), name="currencies" ),
]