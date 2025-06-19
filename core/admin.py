from django.contrib import admin
from .models import (
    NavigationItem,
    FooterInfo,
    FooterQuickLink,
    FooterContact,
    SocialLink,
    SiteIdentity
)

admin.site.register(NavigationItem)
admin.site.register(FooterInfo)
admin.site.register(FooterQuickLink)
admin.site.register(FooterContact)
admin.site.register(SocialLink)
admin.site.register(SiteIdentity)
