from django.contrib import admin

from user_login.models import Migration1

# Register your models here. 
@admin.register(Migration1) 
class ModelAdmin(admin.ModelAdmin):
    list_display = ['source','user','passwd','host','port','service_name']