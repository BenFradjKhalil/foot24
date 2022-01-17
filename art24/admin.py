from django.contrib import admin

from .models import Articles,Articles_principale,Articles_secondaire

# Register your models here.

admin.site.register(Articles)
admin.site.register(Articles_principale)
admin.site.register(Articles_secondaire)



