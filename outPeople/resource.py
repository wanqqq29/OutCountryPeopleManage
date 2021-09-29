from import_export import resources
from .models import StudentInformation
#实现导出中文表头
class BaseModelResource(resources.ModelResource):
    def get_export_headers(self):
        vnames = {i.name: i.verbose_name for i in self.Meta.model._meta.fields}
        return [vnames.get(i.split("__")[0], i) for i in super().get_export_headers()]

class infoResources(BaseModelResource):

    class Meta:
        model = StudentInformation