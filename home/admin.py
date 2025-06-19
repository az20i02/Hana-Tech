from django.contrib import admin
from .models import (
    HeroSection,
    Service,
    MissionSection,
    ImpactSection,
    ImpactStat,
    ImpactHighlight
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'highlighted_text')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MissionSection)
class MissionSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ImpactSection)
class ImpactSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'section', 'order')
    list_filter = ('section',)
    ordering = ('section', 'order')

@admin.register(ImpactHighlight)
class ImpactHighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'link_text')
    list_filter = ('section',)
