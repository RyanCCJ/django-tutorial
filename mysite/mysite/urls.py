from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('post/', views.post),
    path('', views.index),
    path('post/<slug:slug>/', views.showpost),
    path('user/', views.user),
    path('captcha/', include('captcha.urls')),
    path('login/', views.login),
    path('logout/', views.logout),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
