# -*- coding: utf-8 -*-

from django.contrib import admin

from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
