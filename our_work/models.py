from django.db import models

# --- Section 1: Our Work Page Header ---
class WorkIntro(models.Model):
    title = models.CharField(max_length=100, default="Our Work")
    subtitle = models.TextField()

    def __str__(self):
        return self.title

# --- Section 2: Impact Summary (Stats) ---
class WorkImpactOverview(models.Model):
    title = models.CharField(max_length=100, default="Our Impact")
    subtitle = models.TextField()

    def __str__(self):
        return self.title

class WorkImpactStat(models.Model):
    section = models.ForeignKey(WorkImpactOverview, on_delete=models.CASCADE, related_name='stats')
    value = models.CharField(max_length=20)  # e.g. "250+"
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.value} - {self.label}"

# --- Section 3: Featured Work Projects ---
class FeaturedProject(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='our_work/projects/')
    description = models.TextField()

    def __str__(self):
        return self.title

class ProjectHighlight(models.Model):
    project = models.ForeignKey(FeaturedProject, on_delete=models.CASCADE, related_name='highlights')
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"✓ {self.description}"

# --- Section 4: Resources (cards) ---
class EducationalResource(models.Model):
    icon = models.ImageField(upload_to='our_work/resources/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_text = models.CharField(max_length=50, default="Learn More")
    link = models.URLField()

    def __str__(self):
        return self.title
