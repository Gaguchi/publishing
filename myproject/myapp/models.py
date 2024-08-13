from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Template(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to='templates/')