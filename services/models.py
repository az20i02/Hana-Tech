from django.db import models

# General Intro to Services Page
class ServicesIntro(models.Model):
    title = models.CharField(max_length=100, default="Our Services")
    subtitle = models.TextField()

    def __str__(self):
        return self.title


# --- Educational Workshops Section ---

class WorkshopSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return self.title

class Workshop(models.Model):
    section = models.ForeignKey(WorkshopSection, on_delete=models.CASCADE, related_name='workshops')
    icon = models.ImageField(upload_to="services/workshops/")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# --- Legal Support Section ---

class LegalSupportSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class LegalService(models.Model):
    section = models.ForeignKey(LegalSupportSection, on_delete=models.CASCADE, related_name='services')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class LegalSupportContact(models.Model):
    section = models.OneToOneField(LegalSupportSection, on_delete=models.CASCADE, related_name='contact_info')
    text = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"Contact: {self.email}"


# --- Community Support Section ---

class CommunitySupportSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to="services/community/")

    def __str__(self):
        return self.title

class CommunityInitiative(models.Model):
    section = models.ForeignKey(CommunitySupportSection, on_delete=models.CASCADE, related_name='initiatives')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
