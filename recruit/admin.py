from django.contrib import admin
from .models import Application, Estimate, Tag_Type, Tag, Project

# Register your models here.
admin.site.register(Application)
admin.site.register(Estimate)
admin.site.register(Tag_Type)
admin.site.register(Tag)
admin.site.register(Project)