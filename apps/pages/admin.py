from django.contrib import admin

from apps.pages.models import ContactModel, AboutPageModel

admin.site.register(ContactModel)
admin.site.register(AboutPageModel)

