from django.db import models

# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    # date=models.DeteTimeField(auto_now_add=True)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return(self.title)


    def snipetttt(self):
        return self.body[:50]+'...' # '' faramoosh
