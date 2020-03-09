from django.contrib import admin
from .models import Project, ProjectInfo, College, Campus, ProjectActivity

admin.site.register(Project)
admin.site.register(ProjectInfo)
admin.site.register(ProjectActivity)
admin.site.register(Campus)
admin.site.register(College)
