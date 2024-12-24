from django.urls import path
from blog_app import views

urlpatterns = [
    path('home', views.home),
    path('loginn', views.loginn),
    path('', views.signup),
    path('newpost', views.newpost),
    path('mypost', views.mypost),
    path('logout', views.signout),
]