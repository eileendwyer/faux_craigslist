from django.db import models
from django.contrib.auth.models import User
# region don't tie to user
#rename cat to general name
#rename subcat to parent

class Category(models.Model):
    # user = models.ForeignKey("auth.User")
    village = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')


class Posting(models.Model):
    user = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(Category)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)

    class Meta:
        ordering =["-created"]

    def __str__(self):
        return self.title
