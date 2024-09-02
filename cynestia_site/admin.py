from django.contrib import admin
from .models import CustomModel, BlogComment, BlogDetail

# Register your models here.
admin.site.register(CustomModel)
admin.site.register(BlogDetail)
admin.site.register(BlogComment)