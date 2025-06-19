from django.db import models

class MissionIntro(models.Model):
    title = models.CharField(max_length=100, default="Our Mission")
    subtitle = models.TextField()

    def __str__(self):
        return self.title

class Vision(models.Model):
    title = models.CharField(max_length=100, default="Our Vision")
    text = models.TextField()

    def __str__(self):
        return self.title

class Value(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Approach(models.Model):
    section_title = models.CharField(max_length=100, default="Our Approach")
    section_description = models.TextField()

    def __str__(self):
        return self.section_title

class ApproachPillar(models.Model):
    approach = models.ForeignKey(Approach, on_delete=models.CASCADE, related_name='pillars')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
