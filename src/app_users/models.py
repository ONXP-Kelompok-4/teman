from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayName = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayName:
            name = self.displayName
        else:
            name = self.user.username
        return name

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        else:
            return static('images/avatar.svg')