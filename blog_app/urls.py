from django.urls import path
from blog_app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='blog_app/login.html', authentication_form=LoginForm), name='login'),
    path('register/', views.register.as_view(), name="register"),
    path('blogdetail/<int:pk>', views.detail.as_view(), name="detail"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('myblog/', views.Myblogs, name='myblogs'),
    path('postblog/', views.PostBlog.as_view(), name='postblog'),

   
]
    
