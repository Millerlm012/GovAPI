from import_export import resources
from .models import Governor

class GovernorResource(resources.ModelResource):
    class Meta:
        model = Governor
        exclude = ('id',)
