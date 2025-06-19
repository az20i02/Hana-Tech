from django.db import models

# ------------------
# NAVIGATION BAR
# ------------------
class SiteIdentity(models.Model):
    logo = models.ImageField(upload_to="core/logo/")
    site_name = models.CharField(max_length=100, default="Amazonat Libya")
    slogan = models.CharField(max_length=255, default="An aware woman ... a free homeland")

    def __str__(self):
        return self.site_name
        
class NavigationItem(models.Model):
    label = models.CharField(max_length=100)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

# ------------------
# FOOTER
# ------------------

class FooterInfo(models.Model):
    organization_name = models.CharField(max_length=100, default="Amazonat Libya")
    tagline = models.TextField()
    year = models.PositiveIntegerField(default=2025)

    def __str__(self):
        return self.organization_name

class FooterQuickLink(models.Model):
    label = models.CharField(max_length=100)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class FooterContact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class SocialLink(models.Model):
    icon = models.ImageField(upload_to="core/social_icons/")
    platform = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform
