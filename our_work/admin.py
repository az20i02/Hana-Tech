from django.contrib import admin
from .models import (
    WorkIntro, WorkImpactOverview, WorkImpactStat,
    FeaturedProject, ProjectHighlight,
    EducationalResource
)

admin.site.register(WorkIntro)
admin.site.register(WorkImpactOverview)
admin.site.register(WorkImpactStat)
admin.site.register(FeaturedProject)
admin.site.register(ProjectHighlight)
admin.site.register(EducationalResource)
