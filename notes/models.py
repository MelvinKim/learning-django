from django.db import models

# Create your models here. 
class Notes(models.Model):
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.title 