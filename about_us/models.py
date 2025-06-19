from django.db import models

# --- Section 1: About Intro ---
class AboutIntro(models.Model):
    title = models.CharField(max_length=100, default="About Us")
    subtitle = models.TextField()

    def __str__(self):
        return self.title


# --- Section 2: Our Story ---
class OurStory(models.Model):
    title = models.CharField(max_length=100, default="Our Story")
    image = models.ImageField(upload_to='about/story/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title


# --- Section 3: Team Members ---
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='about/team/', blank=True, null=True)

    def __str__(self):
        return self.name


# --- Section 4: Core Values ---
class AboutValue(models.Model):
    icon = models.ImageField(upload_to='about/values/', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


# --- Section 5: Contact Information ---
class ContactInformation(models.Model):
    title = models.CharField(max_length=100, default="Our Contact Information")
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    office_hours = models.CharField(max_length=100)
    map_embed_url = models.URLField(blank=True, help_text="Optional map iframe or link")

    def __str__(self):
        return self.title
