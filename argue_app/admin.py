from django.contrib import admin
from argue_app.models import *
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

# class DataAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
# 	list_display = ()
# 	filter_horizontal = ()
# 	search_fields = []
# 	fields = ()
# 	readonly_fields = ()
# 	list_filter = []
# admin.site.register(Data, DataAdmin)