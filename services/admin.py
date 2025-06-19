from django.contrib import admin
from .models import (
    ServicesIntro,
    WorkshopSection, Workshop,
    LegalSupportSection, LegalService, LegalSupportContact,
    CommunitySupportSection, CommunityInitiative
)

admin.site.register(ServicesIntro)
admin.site.register(WorkshopSection)
admin.site.register(Workshop)
admin.site.register(LegalSupportSection)
admin.site.register(LegalService)
admin.site.register(LegalSupportContact)
admin.site.register(CommunitySupportSection)
admin.site.register(CommunityInitiative)


