from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('panel-admin/', admin.site.urls),
    path('/index', include('backend.apps.allgosnumber.urls')),
    path('', include('backend.apps.account.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)