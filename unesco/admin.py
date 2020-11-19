from django.contrib import admin
from unesco.models import Site,Category,Region,States,Iso
# Register your models here.

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(States)
