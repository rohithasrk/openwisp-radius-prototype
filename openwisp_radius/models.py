from django.db import models
from django_freeradius.base.models import (AbstractNas, AbstractRadiusAccounting, AbstractRadiusBatch,
                                           AbstractRadiusCheck, AbstractRadiusGroupCheck,
                                           AbstractRadiusGroupReply, AbstractRadiusPostAuth,
                                           AbstractRadiusProfile, AbstractRadiusReply,
                                           AbstractRadiusUserGroup, AbstractRadiusUserProfile)

from openwisp_users.mixins import OrgMixin


class RadiusCheck(OrgMixin, AbstractRadiusCheck):
    class Meta(AbstractRadiusCheck.Meta):
        abstract = False


class RadiusAccounting(OrgMixin, AbstractRadiusAccounting):
    class Meta(AbstractRadiusAccounting.Meta):
        abstract = False


class RadiusReply(OrgMixin, AbstractRadiusReply):
    class Meta(AbstractRadiusReply.Meta):
        abstract = False


class RadiusGroupCheck(OrgMixin, AbstractRadiusGroupCheck):
    class Meta(AbstractRadiusGroupCheck.Meta):
        abstract = False


class RadiusGroupReply(OrgMixin, AbstractRadiusGroupReply):
    class Meta(AbstractRadiusGroupReply.Meta):
        abstract = False


class RadiusPostAuth(OrgMixin, AbstractRadiusPostAuth):
    class Meta(AbstractRadiusPostAuth.Meta):
        abstract = False


class RadiusUserGroup(OrgMixin, AbstractRadiusUserGroup):
    class Meta(AbstractRadiusUserGroup.Meta):
        abstract = False


class Nas(OrgMixin, AbstractNas):
    class Meta(AbstractNas.Meta):
        abstract = False


class RadiusBatch(OrgMixin, AbstractRadiusBatch):
    class Meta(AbstractRadiusBatch.Meta):
        abstract = False


class RadiusProfile(OrgMixin, AbstractRadiusProfile):
    class Meta(AbstractRadiusProfile.Meta):
        abstract = False


class RadiusUserProfile(OrgMixin, AbstractRadiusUserProfile):
    class Meta(AbstractRadiusUserProfile.Meta):
        abstract = False
