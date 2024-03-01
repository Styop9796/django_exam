from django.db import models



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    rate=models.FloatField(default=0)
    count=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.rate}"