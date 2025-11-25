# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _
from koalixcrm.plugin import *
from koalixcrm.crm.contact.contact import Contact, ContactCall, ContactVisit,\
    PeopleInlineAdmin, PostalAddressForContact, ContactPostalAddress, \
    ContactPhoneAddress, ContactEmailAddress, CityFilter, StateFilter
from django.contrib.auth.models import User
from koalixcrm.crm.documents.contract import Contract
from koalixcrm.crm.documents.invoice import Invoice
from koalixcrm.crm.documents.quote import Quote


class Customer(Contact):
    default_customer_billing_cycle = models.ForeignKey('CustomerBillingCycle',
                                                       on_delete=models.CASCADE,
                                                       verbose_name=_('Default Billing Cycle'))
    is_member_of = models.ManyToManyField("CustomerGroup",
                                          verbose_name=_('Is member of'),
                                          blank=True)
    is_lead = models.BooleanField(default=True)

    def create_contract(self, user: 'User') -> 'Contract':
        contract = Contract()
        contract.create_from_reference(self, user)
        return contract

    def create_invoice(self, user: 'User') -> 'Invoice':
        contract = self.create_contract(user)
        invoice = contract.create_invoice()
        return invoice

    def create_quote(self, user: 'User') -> 'Quote':
        contract = self.create_contract(user)
        quote = contract.create_quote()
        return quote

    def is_in_group(self, customer_group):
        for customer_group_membership in self.is_member_of.all():
            if customer_group_membership.id == customer_group.id:
                return 1
        return 0

    class Meta:
        app_label = "crm"
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return str(self.id) + ' ' + self.name


class IsLeadFilter(admin.SimpleListFilter):
    title = _('Is lead')
    parameter_name = 'is_lead'

    def lookups(self, request, model_admin):
        return (
            ('lead', _('Lead')),
            ('customer', _('Customer')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'lead':
            return queryset.filter(is_lead=True)
        elif self.value() == 'customer':
            return queryset.filter(is_lead=False)
        else:
            return queryset


class OptionCustomer(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'default_customer_billing_cycle',
                    'get_state',
                    'get_town',
                    'date_of_creation',
                    'get_is_lead',)
    list_filter = ('is_member_of', StateFilter, CityFilter, IsLeadFilter)
    fieldsets = (('', {'fields': ('name',
                                  'default_customer_billing_cycle',
                                  'is_member_of',)}),)
    allow_add = True
    ordering = ('id',)
    search_fields = ('id', 'name')
    inlines = [ContactPostalAddress,
               ContactPhoneAddress,
               ContactEmailAddress,
               PeopleInlineAdmin,
               ContactCall,
               ContactVisit]
    pluginProcessor = PluginProcessor()
    inlines.extend(pluginProcessor.getPluginAdditions("customerInline"))

    @staticmethod
    def get_postal_address(obj):
        return PostalAddressForContact.objects.filter(person=obj.id).first()

    def get_state(self, obj):
        address = self.get_postal_address(obj)
        return address.state if address is not None else None

    get_state.short_description = _("State")

    def get_town(self, obj):
        address = self.get_postal_address(obj)
        return address.town if address is not None else None

    get_town.short_description = _("City")

    @staticmethod
    def get_is_lead(obj):
        return obj.is_lead

    get_is_lead.short_description = _("Is Lead")

    def create_contract(self, request, queryset):
        if queryset.count() == 1:
            contract = queryset[0].create_contract(request.user)
            return HttpResponseRedirect('/admin/crm/contract/' + str(contract.id))
        else:
            for obj in queryset:
                obj.create_contract(request.user)
            self.message_user(request, _("%s contracts created" % queryset.count()))

    create_contract.short_description = _("Create Contract")

    def create_quote(self, request, queryset):
        if queryset.count() == 1:
            quote = queryset[0].create_quote(request.user)
            return HttpResponseRedirect('/admin/crm/quote/' + str(quote.id))
        else:
            for obj in queryset:
                obj.create_quote(request.user)
            self.message_user(request, _("%s quotes created" % queryset.count()))

    create_quote.short_description = _("Create Quote")

    def create_invoice(self, request, queryset):
        if queryset.count() == 1:
            invoice = queryset[0].create_invoice(request.user)
            return HttpResponseRedirect('/admin/crm/invoice/' + str(invoice.id))
        else:
            for obj in queryset:
                obj.create_invoice(request.user)
            self.message_user(request, _("%s invoices created" % queryset.count()))

    create_invoice.short_description = _("Create Invoice")

    def save_model(self, request, obj, form, change):
        obj.last_modified_by = request.user
        obj.save()

    actions = ['create_contract', 'create_invoice', 'create_quote']
    pluginProcessor = PluginProcessor()
    inlines.extend(pluginProcessor.getPluginAdditions("customerActions"))
