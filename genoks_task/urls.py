"""
URL configuration for genoks_task project.

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
import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve
from dotenv import load_dotenv
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = "Genoks Task Kitapçı Admin Paneli"  # Site başlığı
admin.site.site_url = "/admin/"  # Site başlık URL'ini değiştirme
admin.site.index_title = "Genoks Task Kitapçı Admin"  # Index başlığı

load_dotenv()

schema_view = get_schema_view(
    openapi.Info(
        title="Genoks Task API",
        default_version='v1',
        description="Genoks Kitapcı API lerine buradan ulaşabilirsiniz.",
        terms_of_service="http://127.0.0.1:8000/api",
        contact=openapi.Contact(email="omersaidbuldukk@gmail.com"),
        license=openapi.License(name="BSD License"),
        base_url=os.getenv('SCHEMA_BASE_URL'),
    ),
    url=os.getenv('SCHEMA_BASE_URL'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"api/writer/", include('writer.urls'), name='writer'),
    path(f"api/books/", include('books.urls'), name='books'),
    path(f"api/sales/", include('sales.urls'), name='sales'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view().without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^$', RedirectView.as_view(url='/swagger/')),
    re_path(r'^redoc/$', schema_view().with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,
                                              'show_indexes': settings.DEBUG}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,
                                             'show_indexes': settings.DEBUG}),
]
