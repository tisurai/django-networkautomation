from django.contrib import admin
from webconfigapp.models import Routers

class RouterAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'hostip', 'ios']

    class Meta:
        model = Routers

admin.site.register(Routers, RouterAdmin)