from django.contrib import admin
from .models import *

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    pass

@admin.register(PriceChange)
class PriceChangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Nameasset)
class NameassetAdmin(admin.ModelAdmin):
    pass

@admin.register(Namemonth)
class NamemonthAdmin(admin.ModelAdmin):
    pass