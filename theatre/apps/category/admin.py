from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'father_name', 'phone_number')


admin.site.register(Teacher, TeacherAdmin)
