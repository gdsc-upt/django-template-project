"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from filebrowser.sites import site
from rest_framework import permissions

from common.urls import common_urls

SchemaView = get_schema_view(
    openapi.Info(
        title=admin.site.site_header + ' API',
        default_version='v1',
        description=admin.site.site_header + ' API description',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='dsc.upt@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/admin/')),
    path('api/grappelli/', include('grappelli.urls')),
    path('api/admin/docs/', include('django.contrib.admindocs.urls')),
    path('api/admin/', admin.site.urls),
    path('api/filebrowser/', site.urls),
    path('api/swagger/', SchemaView.with_ui()),
    path('api/', include(common_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('api/__debug__/', include(debug_toolbar.urls))]
