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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # auth
    path("registration/signup", views.signup, name="signup"),
    path("registration/login", views.login, name="login"),
    path("registration/logout", views.logout, name="logout"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("profile_new/", views.profile_new, name="profile_new"),
    path("profile_edit/<int:user_pk>",views.profile_edit, name="profile_edit"),
    path('author_profile/<int:post_pk>', views.author_profile, name="author_profile"),
    path('regist_page',views.regist_page,name="regist_page"),

    path('home/fotd',views.home_fotd, name="home_fotd"),
    path('home/ootd',views.home_ootd, name="home_ootd"),
    path('home/motd',views.home_motd, name="home_motd"),
    path('home/totd',views.home_totd, name="home_totd"),

    # path('event/new/', views.event, name="new"),

    path('<int:year>/<int:month>/<int:day>/new/fotd',views.new_fotd, name="new_fotd"),
    path('<int:year>/<int:month>/<int:day>/new/ootd',views.new_ootd, name="new_ootd"),
    path('<int:year>/<int:month>/<int:day>/new/motd',views.new_motd, name="new_motd"),
    path('<int:year>/<int:month>/<int:day>/new/totd',views.new_totd, name="new_totd"),

    path('home/main_detail/<int:year>/<int:month>/<int:day>',views.main_detail, name="main_detail"),

    path('<int:year>/<int:month>/<int:day>/edit/fotd/<int:fotd_pk>',views.edit_fotd, name="edit_fotd"),
    path('<int:year>/<int:month>/<int:day>/edit/ootd/<int:ootd_pk>',views.edit_ootd, name="edit_ootd"),
    path('<int:year>/<int:month>/<int:day>/edit/motd/<int:motd_pk>',views.edit_motd, name="edit_motd"),
    path('<int:year>/<int:month>/<int:day>/edit/totd/<int:totd_pk>',views.edit_totd, name="edit_totd"),

    path('<int:year>/<int:month>/<int:day>/delete/fotd/<int:fotd_pk>',views.delete_fotd, name="delete_fotd"),
    path('<int:year>/<int:month>/<int:day>/delete/ootd/<int:ootd_pk>',views.delete_ootd, name="delete_ootd"),
    path('<int:year>/<int:month>/<int:day>/delete/motd/<int:motd_pk>',views.delete_motd, name="delete_motd"),
    path('<int:year>/<int:month>/<int:day>/delete/totd/<int:totd_pk>',views.delete_totd, name="delete_totd"),

    path('<int:year>/<int:month>/<int:day>/detail/fotd/<int:fotd_pk>',views.detail_fotd, name="detail_fotd"),
    path('<int:year>/<int:month>/<int:day>/detail/ootd/<int:ootd_pk>',views.detail_ootd, name="detail_ootd"),
    path('<int:year>/<int:month>/<int:day>/detail/motd/<int:motd_pk>',views.detail_motd, name="detail_motd"),
    path('<int:year>/<int:month>/<int:day>/detail/totd/<int:totd_pk>',views.detail_totd, name="detail_totd"),

    path('like/fotd', views.like_fotd ,name="like_fotd"),
    path('like/ootd', views.like_ootd ,name="like_ootd"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
