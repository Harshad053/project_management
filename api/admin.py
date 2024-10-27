from django.contrib import admin
from .models import Client
from django.contrib.auth.models import User

class ClientAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = User.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Client, ClientAdmin)

