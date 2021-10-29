from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Student,Teacher,Grade,Module


admin.site.register(User)

admin.site.register(Student)

admin.site.register(Teacher)

admin.site.register(Grade)

admin.site.register(Module)

