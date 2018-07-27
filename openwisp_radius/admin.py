from django.contrib import admin
from django_freeradius.base.admin import *

from openwisp_users.admin import UserAdmin
from openwisp_utils.admin import MultitenantAdminMixin, MultitenantOrgFilter, MultitenantRelatedOrgFilter

from .models import *


@admin.register(RadiusCheck)
class RadiusCheckAdmin(MultitenantAdminMixin, AbstractRadiusCheckAdmin):
    pass


RadiusCheckAdmin.fields.append('organization')


@admin.register(RadiusReply)
class RadiusReplyAdmin(MultitenantAdminMixin, AbstractRadiusReplyAdmin):
    pass


@admin.register(RadiusAccounting)
class RadiusAccountingAdmin(MultitenantAdminMixin, AbstractRadiusAccountingAdmin):
    pass

@admin.register(Nas)
class NasAdmin(MultitenantAdminMixin, AbstractNasAdmin):
    pass


@admin.register(RadiusUserGroup)
class RadiusUserGroupAdmin(MultitenantAdminMixin, AbstractRadiusUserGroupAdmin):
    pass


@admin.register(RadiusGroupReply)
class RadiusGroupReplyAdmin(MultitenantAdminMixin, AbstractRadiusGroupReplyAdmin):
    pass


@admin.register(RadiusGroupCheck)
class RadiusGroupCheckAdmin(MultitenantAdminMixin, AbstractRadiusGroupCheckAdmin):
    pass


@admin.register(RadiusPostAuth)
class RadiusPostAuthAdmin(MultitenantAdminMixin, AbstractRadiusPostAuthAdmin):
    pass


@admin.register(RadiusBatch)
class RadiusBatchAdmin(MultitenantAdminMixin, AbstractRadiusBatchAdmin):
    pass


@admin.register(RadiusProfile)
class RadiusProfileAdmin(MultitenantAdminMixin, AbstractRadiusProfileAdmin):
    pass


class RadiusUserProfileInline(AbstractRadiusUserProfileInline):
    model = RadiusUserProfile


UserAdmin.inlines.append(RadiusUserProfileInline)
