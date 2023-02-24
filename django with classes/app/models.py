from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    text=models.TextField()
    title=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    