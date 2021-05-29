from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "create_at"]
    list_display_links = ("name",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(Social)
