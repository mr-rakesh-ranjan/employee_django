from django.contrib import admin
from .models import Employee
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','phone', 'address' )
    search_fields = ('first_name',)
    list_editable=('phone',)


admin.site.register(Employee, EmpAdmin)
