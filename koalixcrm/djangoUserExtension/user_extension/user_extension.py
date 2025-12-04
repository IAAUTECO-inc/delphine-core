# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _

from koalixcrm.djangoUserExtension.placeholders import PostalAddress
from koalixcrm.djangoUserExtension.placeholders import PhoneAddress
from koalixcrm.djangoUserExtension.placeholders import EmailAddress
from koalixcrm.djangoUserExtension.const.purpose import *
from koalixcrm.djangoUserExtension.exceptions import *
from koalixcrm.global_support_functions import xstr


class UserExtension(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("auth.User",
                             on_delete=models.CASCADE,
                             blank=False,
                             null=False)
    default_template_set = models.ForeignKey("TemplateSet", on_delete=models.CASCADE)
    default_currency = models.ForeignKey("Currency", on_delete=models.CASCADE)

    @staticmethod
    def objects_to_serialize(object_to_create_pdf, reference_user):
        from koalixcrm.djangoUserExtension import services
        return services.objects_to_serialize(object_to_create_pdf, reference_user)

    @staticmethod
    def get_user_extension(django_user):
        from koalixcrm.djangoUserExtension import services
        return services.get_user_extension(django_user)

    def get_template_set(self, template_set):
        from koalixcrm.djangoUserExtension import services
        return services.get_template_set(self, template_set)

    def get_fop_config_file(self, template_set):
        from koalixcrm.djangoUserExtension import services
        return services.get_fop_config_file(self, template_set)

    def get_xsl_file(self, template_set):
        from koalixcrm.djangoUserExtension import services
        return services.get_xsl_file(self, template_set)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('User Extension')
        verbose_name_plural = _('User Extension')

    def __str__(self):
        return xstr(self.id) + ' ' + xstr(self.user.__str__())


class UserExtensionPostalAddress(PostalAddress):
    purpose = models.CharField(verbose_name=_("Purpose"), max_length=1, choices=PURPOSESADDRESSINUSEREXTENTION)
    userExtension = models.ForeignKey(UserExtension, on_delete=models.CASCADE)

    def __str__(self):
        return xstr(self.name) + ' ' + xstr(self.pre_name)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Postal Address for User Extension')
        verbose_name_plural = _('Postal Address for User Extension')


class UserExtensionPhoneAddress(PhoneAddress):
    purpose = models.CharField(verbose_name=_("Purpose"), max_length=1, choices=PURPOSESADDRESSINUSEREXTENTION)
    userExtension = models.ForeignKey(UserExtension, on_delete=models.CASCADE)

    def __str__(self):
        return xstr(self.phone)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Phone number for User Extension')
        verbose_name_plural = _('Phone number for User Extension')


class UserExtensionEmailAddress(EmailAddress):
    purpose = models.CharField(verbose_name=_("Purpose"), max_length=1, choices=PURPOSESADDRESSINUSEREXTENTION)
    userExtension = models.ForeignKey(UserExtension, on_delete=models.CASCADE)

    def __str__(self):
        return xstr(self.email)

    class Meta:
        app_label = "djangoUserExtension"
        verbose_name = _('Email Address for User Extension')
        verbose_name_plural = _('Email Address for User Extension')



