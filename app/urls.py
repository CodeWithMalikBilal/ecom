"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import View
from app import views
from django.contrib.auth import views as auth_view
from .forms import CustomerLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ProductView.as_view(),name="home"),
    path('menu',views.MenuView.as_view(),name='menu'),
    path('about',views.aboutus,name="about"),
    path('order',views.order,name="order"),
    path('contact',views.contact,name="contact"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=CustomerLoginForm),name='login'),
    #path("login",views.login,name="login"),
    path('register',views.CustomerRegisterView.as_view(),name="register"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name="product-detail"),
    path('add-to-cart/',views.addtocart,name="add-to-cart"),
    path('cart/',views.showcart,name='showcart'),
    path('pluscart/',views.pluscart),
    path('minuscart/',views.minuscart),
    path('removecart/',views.removecart),
    #path('showcart/',views.showcart,name="showcart"),
    path('logout',views.logout_user,name='logout'),
    path('address',views.address,name='address'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
