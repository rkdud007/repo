from django.shortcuts import render,redirect
from .models import Fotd,Ootd,Tag,Totd,Motd,Profile,Like_Fotd,Like_Ootd
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup():
def login():
def logout():
def profile_new():
def profile_edit():
def my_profile():
def author_profile():

def home(request):
    fotd  =Fotd.objects.all()
    ootd = Ootd.objects.all()
    totd = Totd.objects.all()
    motd = Motd.objects.all()
    return render(request, "home.html", {"posts": posts})


def new_fotd():
def new_ootd():
def new_motd():
def new_totd():
def detail_fotd():
def detail_ootd():
def detail_motd():
def detail_totd():
def edit_fotd():
def edit_ootd():
def edit_motd():
def edit_totd():
def delete_fotd():
def delete_ootd():
def delete_motd():
def delete_totd():
