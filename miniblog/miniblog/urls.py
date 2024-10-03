from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.About_view, name='about-page'),
    path('contact/', views.contact_view, name='contact-page'),
    path('dashboard/', views.dashboard_view, name='dashboard-page'),
    path('signup/', views.signup_view, name='signup-page'),
    path('login/', views.login_view, name='login-page'),
    path('logout/', views.logout_view, name='logout-page'),
    path('addpost/', views.add_post, name='addpost'),
    path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    path('deletepost/<int:id>/', views.delete_post, name='deletepost'),

]
