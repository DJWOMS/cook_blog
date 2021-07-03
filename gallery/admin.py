from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Photo, Gallery


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "get_image")
    readonly_fields = ("get_image",)
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')


@admin.register(Gallery)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date")
