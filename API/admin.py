from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import Currencies

admin.site.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
	list_display = ("currency", "buying", "sales", "code",)
