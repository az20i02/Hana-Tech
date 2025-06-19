from django.db import models

# Section 1: Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    highlighted_text = models.CharField(max_length=100)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to="hero/", blank=True, null=True)
    primary_button_text = models.CharField(max_length=50)
    primary_button_link = models.URLField()
    secondary_button_text = models.CharField(max_length=50, blank=True)
    secondary_button_link = models.URLField(blank=True)

    def __str__(self):
        return f"Hero: {self.title}"

# Section 2: Services
class Service(models.Model):
    icon = models.ImageField(upload_to="services/icons/")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_text = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title

# Section 3: Mission
class MissionSection(models.Model):
    title = models.CharField(max_length=100, default="Our Mission")
    description = models.TextField()
    image = models.ImageField(upload_to="mission/")
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()

    def __str__(self):
        return self.title


# Section 4: Impact Section
class ImpactSection(models.Model):
    title = models.CharField(max_length=100, default="Our Impact")
    description = models.TextField()

    def __str__(self):
        return self.title



class ImpactStat(models.Model):
    section = models.ForeignKey(ImpactSection, on_delete=models.CASCADE, related_name='stats')
    value = models.CharField(max_length=20)  # e.g., "250+"
    label = models.CharField(max_length=100)  # e.g., "Workshops Conducted"
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.label}"



class ImpactHighlight(models.Model):
    section = models.ForeignKey(ImpactSection, on_delete=models.CASCADE, related_name='highlights')
    icon = models.ImageField(upload_to="impact/icons/")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_text = models.CharField(max_length=50, default="Read More")
    link = models.URLField()

    def __str__(self):
        return self.title
