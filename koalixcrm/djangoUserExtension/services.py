# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from koalixcrm.djangoUserExtension.exceptions import UserExtensionMissing, TooManyUserExtensionsAvailable, \
    TemplateSetMissingForUserExtension, UserExtensionPhoneAddressMissing, UserExtensionEmailAddressMissing


def objects_to_serialize(object_to_create_pdf, reference_user):
    from koalixcrm.djangoUserExtension.placeholders import PhoneAddress, EmailAddress
    from django.contrib import auth
    from koalixcrm.djangoUserExtension.models import UserExtension, UserExtensionPhoneAddress, UserExtensionEmailAddress
    objects = list(auth.models.User.objects.filter(id=reference_user.id))
    user_extension = UserExtension.objects.filter(user=reference_user.id)
    if len(user_extension) == 0:
        raise UserExtensionMissing(_("During "+str(object_to_create_pdf)+" PDF Export"))
    phone_address = UserExtensionPhoneAddress.objects.filter(
        userExtension=user_extension[0].id)
    if len(phone_address) == 0:
        raise UserExtensionPhoneAddressMissing(_("During "+str(object_to_create_pdf)+" PDF Export"))
    email_address = UserExtensionEmailAddress.objects.filter(
        userExtension=user_extension[0].id)
    if len(email_address) == 0:
        raise UserExtensionEmailAddressMissing(_("During "+str(object_to_create_pdf)+" PDF Export"))
    objects += list(user_extension)
    objects += list(EmailAddress.objects.filter(id=email_address[0].id))
    objects += list(PhoneAddress.objects.filter(id=phone_address[0].id))
    return objects


def get_user_extension(django_user):
    from koalixcrm.djangoUserExtension.models import UserExtension
    user_extensions = UserExtension.objects.filter(user=django_user)
    if len(user_extensions) > 1:
        raise TooManyUserExtensionsAvailable(_("More than one User Extension define for user ") + django_user.__str__())
    elif len(user_extensions) == 0:
        raise UserExtensionMissing(_("No User Extension define for user ") + django_user.__str__())
    return user_extensions[0]


def get_template_set(user_extension, template_set):
    if template_set == user_extension.default_template_set.work_report_template:
        if user_extension.default_template_set.work_report_template:
            return user_extension.default_template_set.work_report_template
        else:
            raise TemplateSetMissingForUserExtension((_("Template Set for work report " +
                                                        "is missing for User Extension" + str(user_extension))))


def get_fop_config_file(user_extension, template_set):
    template_set = get_template_set(user_extension, template_set)
    return template_set.get_fop_config_file()

def get_xsl_file(user_extension, template_set):
    template_set = get_template_set(user_extension, template_set)
    return template_set.get_xsl_file()
