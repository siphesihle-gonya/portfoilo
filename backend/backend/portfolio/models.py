from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")  # <-- this must exist!
    image = models.ImageField(upload_to="projects/")
    live_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

