# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _

from filebrowser.fields import FileBrowseField

from koalixcrm.djangoUserExtension.user_extension.text_paragraph import InlineTextParagraph
from koalixcrm.global_support_functions import xstr
from koalixcrm.djangoUserExtension.exceptions import TemplateFOPConfigFileMissing, TemplateXSLTFileMissing


class DocumentTemplate(models.Model):
    INVOICE = "INV"
    QUOTE = "QUO"
    DELIVERY_NOTE = "DLN"
    PAYMENT_REMINDER = "PRM"
    PURCHASE_ORDER = "PUO"
    PURCHASE_CONFIRMATION = "PUC"
    PROFIT_LOSS_STATEMENT = "PLS"
    BALANCE_SHEET = "BSH"
    MONTHLY_PROJECT_SUMMARY = "MPS"
    WORK_REPORT = "WRP"

    TEMPLATE_TYPES = (
        (INVOICE, _("Invoice")),
        (QUOTE, _("Quote")),
        (DELIVERY_NOTE, _("Delivery Note")),
        (PAYMENT_REMINDER, _("Payment Reminder")),
        (PURCHASE_ORDER, _("Purchase Order")),
        (PURCHASE_CONFIRMATION, _("Purchase Confirmation")),
        (PROFIT_LOSS_STATEMENT, _("Profit Loss Statement")),
        (BALANCE_SHEET, _("Balance Sheet")),
        (MONTHLY_PROJECT_SUMMARY, _("Monthly Project Summary")),
        (WORK_REPORT, _("Work Report")),
    )

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name=_("Title"),
                             max_length=100,
                             blank=True,
                             null=True)
    template_type = models.CharField(max_length=3, choices=TEMPLATE_TYPES, verbose_name=_("Template Type"))
    xsl_file = FileBrowseField(verbose_name=_("XSL File"),
                               max_length=200)
    fop_config_file = FileBrowseField(verbose_name=_("FOP Configuration File"),
                                      blank=True,
                                      null=True,
                                      max_length=200)
    logo = FileBrowseField(verbose_name=_("Logo for the PDF generation"),
                           blank=True,
                           null=True,
                           max_length=200)

    def get_fop_config_file(self):
        if self.fop_config_file:
            return self.fop_config_file
        else:
            raise TemplateFOPConfigFileMissing(_("Fop Config File missing in Document Template"+str(self)))

    def get_xsl_file(self):
        if self.xsl_file:
            return self.xsl_file
        else:
            raise TemplateXSLTFileMissing(_("XSL Template missing in Document Template"+str(self)))

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Document template')
        verbose_name_plural = _('Document templates')

    def __str__(self):
        return xstr(self.id) + ' ' + xstr(self.title.__str__())




