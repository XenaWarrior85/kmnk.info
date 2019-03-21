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

from person import views
from app_registration import views as wi
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from app_kmnk_main import views as kmnk_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', views.PersonView.as_view(), name='person_main'),
    path('person/<int:id>/', views.person, name='person'),
    path('person/<int:id>/add', views.add_person, name='add_person'),
    path('person/<int:id>/edit', views.edit_person, name='edit_person'),
    path('login/', wi.MyLoginView, name='authapp-login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='authapp-logout'),
    path('registration/', wi.registration, name="signup"),
    path('admin_view/', wi.admin_add_person, name="admin_view"),
    path('', kmnk_view.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
