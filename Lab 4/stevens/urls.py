from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from myapp import views

admin.autodiscover()

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(
                        url=staticfiles_storage.url('favicon.ico'),
                        permanent=False), name="favicon"),
    path('', views.home, name='home'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
