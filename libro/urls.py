from django.contrib import admin
from django.urls import path
from info import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
