from django.db import models

class Image(models.Model):
    SECTION_CHOICES = [
        ('section1', 'Section 1'),
        ('section2', 'Section 2'),
    ]
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True)