# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _


class PlaceholderAddress(models.Model):
    class Meta:
        abstract = True


class PostalAddress(PlaceholderAddress):
    name = models.CharField(max_length=100, blank=True, null=True)
    pre_name = models.CharField(max_length=100, blank=True, null=True)
    address_line_1 = models.CharField(max_length=200, blank=True, null=True)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    address_line_3 = models.CharField(max_length=200, blank=True, null=True)
    address_line_4 = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    prefix = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Postal Address')
        verbose_name_plural = _('Postal Address')


class PhoneAddress(PlaceholderAddress):
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Phone Address')
        verbose_name_plural = _('Phone Address')


class EmailAddress(PlaceholderAddress):
    email = models.EmailField(max_length=200, blank=True, null=True)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Email Address')
        verbose_name_plural = _('Email Address')


class Currency(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
