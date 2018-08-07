from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import signals
from django_freeradius.base.models import (AbstractNas, AbstractRadiusAccounting, AbstractRadiusBatch,
                                           AbstractRadiusCheck, AbstractRadiusGroupCheck,
                                           AbstractRadiusGroupReply, AbstractRadiusPostAuth,
                                           AbstractRadiusProfile, AbstractRadiusReply,
                                           AbstractRadiusUserGroup, AbstractRadiusUserProfile)
from django_freeradius.utils import set_default_limits

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
    def _create_user_profile(self, **kwargs):
        options = dict(organization=self.organization)
        options.update(kwargs)
        return super(RadiusProfile, self)._create_user_profile(**options)

    class Meta(AbstractRadiusProfile.Meta):
        abstract = False


class RadiusUserProfile(OrgMixin, AbstractRadiusUserProfile):
    def _create_radcheck(self, **kwargs):
        options = dict(organization=self.organization)
        options.update(kwargs)
        return super(RadiusUserProfile, self)._create_radcheck(**options)

    class Meta(AbstractRadiusUserProfile.Meta):
        abstract = False


signals.post_save.connect(set_default_limits, sender=get_user_model())
