
from django.contrib import admin

from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('authentification/',include('authentification.urls')),
    path('actualite/',include('actualite.urls')),
    path('contact/',include('contact.urls'))

] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
