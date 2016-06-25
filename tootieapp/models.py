from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# region don't tie to user
#rename cat to general name
#rename subcat to parent

class Village(models.Model):
    village_name = models.CharField(max_length=30)

class Category(models.Model):
    # user = models.ForeignKey("auth.User")
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')


class Posting(models.Model):
    user = models.ForeignKey("auth.User")
    village = models.ForeignKey(Village)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)

    class Meta:
        ordering =["-created"]

    def __str__(self):
        return self.title

class Profile(models.Model):

    user = models.OneToOneField("auth.user")
    favorite_village = models.ForeignKey(Village)
    photo = models.ImageField(upload_to="profile_photo", null=True, blank=True, verbose_name="profile_photo")

@property
def photo_url(self):
    if self.photo:
        # print(self.photo.url)
        return self.photo.url
    # return http://

@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)
