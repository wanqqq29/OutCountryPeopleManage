import collections

import tablib
from django.contrib.auth.models import User
from django.db import models
from import_export import resources
from outpeopleCheckin.models import Tinfo, Cinfo, SCinfo,Sinfo
from django.apps import apps
#实现导出中文表头
class BaseModelResource(resources.ModelResource):
    def get_export_headers(self):
        vnames = {i.name: i.verbose_name for i in self.Meta.model._meta.fields}
        return [vnames.get(i.split("__")[0], i) for i in super().get_export_headers()]

class abroadResource(BaseModelResource):
    class Meta:
        model = Cinfo

class SabroadResource(BaseModelResource):
    class Meta:
        model = SCinfo

class SinfoR(BaseModelResource):
    class Meta:
        model = Sinfo


class TinfoR(BaseModelResource):
    class Meta:
        model = Tinfo