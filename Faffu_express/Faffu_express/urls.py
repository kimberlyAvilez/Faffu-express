"""
archivo principal de la URL
"""
from django.contrib import admin
from django.urls import path
from aplicacion.Principal import views
from login import views as login_views

from django.conf import settings

urlpatterns = [
    path('', login_views.login, name="Login"),
    path('admin/', admin.site.urls),
]
