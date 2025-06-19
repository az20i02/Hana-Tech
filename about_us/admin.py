from django.contrib import admin
from .models import (
    AboutIntro,
    OurStory,
    TeamMember,
    AboutValue,
    ContactInformation
)

admin.site.register(AboutIntro)
admin.site.register(OurStory)
admin.site.register(TeamMember)
admin.site.register(AboutValue)
admin.site.register(ContactInformation)
