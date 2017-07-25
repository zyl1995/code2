from django.contrib import admin

# Register your models here.
from rango.models import Lategory, Page, UserProfile
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
class LategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Lategory, LategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


