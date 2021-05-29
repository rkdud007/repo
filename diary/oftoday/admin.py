from django.contrib import admin
from .models import Fotd,Ootd,Tag,Totd,Motd,Profile,Like_Fotd,Like_Ootd

# Register your models here.
admin.site.register(Fotd)
admin.site.register(Ootd)
admin.site.register(Tag)
admin.site.register(Totd)
admin.site.register(Motd)
admin.site.register(Profile)
admin.site.register(Like_Fotd)
admin.site.register(Like_Ootd)
