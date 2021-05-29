"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from oftoday import views

urlpatterns = [
    path("registration/signup", views.signup, name="signup"),
    path("registration/login", views.login, name="login"),
    path("registration/logout", views.logout, name="logout"),
    path("accounts/", include("allauth.urls")),

    path('admin/', admin.site.urls),
    path("profile_new/", views.profile_new, name="profile_new"),
    path("profile_edit/<int:user_pk>",views.profile_edit, name="profile_edit"),
    path("my_profile/<int:user_pk>" ,views.my_profile, name = "my_profile"),
    path('author_profile/<int:post_pk>', views.author_profile, name="author_profile"),

    path('',views.home, name="home"),
    # new
    path('new/fotd',views.new_fotd, name="new_fotd"),
    path('new/ootd',views.new_ootd, name="new_ootd"),
    path('new/motd',views.new_motd, name="new_motd"),
    path('new/totd',views.new_totd, name="new_totd"),
    #detail
    path('detail/fotd/<int:fotd_pk>',views.detail_fotd, name="detail_fotd"),
    path('detail/ootd/<int:ootd_pk>',views.detail_ootd, name="detail_ootd"),
    path('detail/motd/<int:motd_pk>',views.detail_motd, name="detail_motd"),
    path('detail/totd/<int:totd_pk>',views.detail_totd, name="detail_totd"),
    #edit
    path('edit/fotd/<int:fotd_pk>',views.edit_fotd, name="edit_fotd"),
    path('edit/ootd/<int:ootd_pk>',views.edit_ootd, name="edit_ootd"),
    path('edit/motd/<int:motd_pk>',views.edit_motd, name="edit_motd"),
    path('edit/totd/<int:totd_pk>',views.edit_totd, name="edit_totd"),
    #delete
    path('delete/fotd/<int:fotd_pk>',views.delete_fotd, name="delete_fotd"),
    path('delete/ootd/<int:ootd_pk>',views.delete_ootd, name="delete_ootd"),
    path('delete/motd/<int:motd_pk>',views.delete_motd, name="delete_motd"),
    path('delete/totd/<int:totd_pk>',views.delete_totd, name="delete_totd"),

    path('like', views.like ,name="like") 
]
