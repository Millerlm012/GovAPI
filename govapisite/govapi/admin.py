from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Governor

# Register your models here.
#admin.site.register(Governor)

@admin.register(Governor)
class GovernorAdmin(ImportExportModelAdmin):
    pass
