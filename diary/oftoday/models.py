from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class Fotd(models.Model):
    picture = models.ImageField(blank = True)
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    share = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag',blank=True)
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ootd(models.Model):
    picture = models.ImageField(blank = True)
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    share = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag',blank=True)
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Totd(models.Model):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black")
    ]
    title = models.CharField(max_length=100,default="")
    content = models.TextField(max_length=300,default="")
    color = ColorField(choices=COLOR_CHOICES)
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

class Motd(models.Model):
    OPTIONS = (
        ('1', '행벅'),
        ('2', '꿀꿀'),
        ('3', '짜증'),
        ('4', '우울'),
        ('5', '평온'),
        ('6', '나도 날 몰라')
    )

    title = models.CharField(max_length=100,default="")
    moods = models.CharField(choices=OPTIONS,max_length=50)
    content = models.TextField(max_length=1000,default="")
    day = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True,default="")
    image = models.ImageField(blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.nickname

class Like_Fotd(models.Model):
    fotd = models.ForeignKey(
        Fotd, on_delete=models.CASCADE, related_name= "like_fotd"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE ,related_name="like_fotd"
    )

class Like_Ootd(models.Model):
    ootd = models.ForeignKey(
        Ootd, on_delete=models.CASCADE, related_name= "like_ootd"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE ,related_name="like_ootd"
    )