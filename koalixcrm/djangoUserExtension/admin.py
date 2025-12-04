# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext as _

from koalixcrm.djangoUserExtension.user_extension.user_extension import UserExtension, UserExtensionPostalAddress, \
    UserExtensionPhoneAddress, UserExtensionEmailAddress
from koalixcrm.djangoUserExtension.user_extension.template_set import TemplateSet
from koalixcrm.djangoUserExtension.user_extension.document_template import DocumentTemplate
from koalixcrm.djangoUserExtension.user_extension.text_paragraph import InlineTextParagraph


class InlineUserExtensionPostalAddress(admin.StackedInline):
    model = UserExtensionPostalAddress
    extra = 1
    classes = ('collapse-open',)
    fieldsets = (
        (_('Basics'), {
            'fields': (
                'prefix',
                'pre_name',
                'name',
                'address_line_1',
                'address_line_2',
                'address_line_3',
                'address_line_4',
                'zip_code',
                'town',
                'state',
                'country',
                'purpose')
        }),
    )
    allow_add = True


class InlineUserExtensionPhoneAddress(admin.StackedInline):
    model = UserExtensionPhoneAddress
    extra = 1
    classes = ('collapse-open',)
    fieldsets = (
        (_('Basics'), {
            'fields': ('phone',
                       'purpose',)
        }),
    )
    allow_add = True


class InlineUserExtensionEmailAddress(admin.StackedInline):
    model = UserExtensionEmailAddress
    extra = 1
    classes = ('collapse-open',)
    fieldsets = (
        (_('Basics'), {
            'fields': ('email',
                       'purpose',)
        }),
    )
    allow_add = True


class OptionUserExtension(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'default_template_set',
                    'default_currency')
    list_display_links = ('id',
                          'user')
    list_filter = ('user',
                   'default_template_set',)
    ordering = ('id',)
    search_fields = ('id',
                     'user')
    fieldsets = (
        (_('Basics'), {
            'fields': ('user',
                       'default_template_set',
                       'default_currency')
        }),
    )
    inlines = [InlineUserExtensionPostalAddress,
               InlineUserExtensionPhoneAddress,
               InlineUserExtensionEmailAddress]


class OptionDocumentTemplate(admin.ModelAdmin):
    list_display = ('id', 'title', 'template_type')
    list_display_links = ('id', 'title')
    ordering = ('id',)
    search_fields = ('id', 'title')
    fieldsets = (
        (_('Basics'), {
            'fields': ('title',
                       'template_type',
                       'xsl_file',
                       'fop_config_file',
                       'logo')
        }),
    )
    inlines = [InlineTextParagraph]


admin.site.register(UserExtension, OptionUserExtension)
admin.site.register(DocumentTemplate, OptionDocumentTemplate)
admin.site.register(TemplateSet)