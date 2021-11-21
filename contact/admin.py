from django.contrib import admin

from .models import ContactModel, ContactLink, AboutModel, SocialModel, ImageAboutModel


class ImageAboutInline(admin.StackedInline):
    model = ImageAboutModel
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "create_at"]
    list_display_links = ("name",)


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(SocialModel)
