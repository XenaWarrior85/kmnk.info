"""kmnk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import url
from person import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from kmnk_main import views
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import views as auth_views


urlpatterns = [
    path ('', include('kmnk_main.urls')),
    path ('admin/', admin.site.urls),
    path ('<int:id>/', views.person, name='person'),
    path ('<int:id>/add', views.add_person, name='add_person'),
    path ('<int:id>/edit', views.edit_person, name='edit_person'),
    path ('login/', LoginView.as_view (template_name='login.html'),
          name='authapp-login'),
    path('logout/', LogoutView.as_view(next_page='/'),
             name='authapp-logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
