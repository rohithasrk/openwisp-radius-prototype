from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from openwisp_utils.admin_theme.admin import admin, openwisp_admin

openwisp_admin()
admin.autodiscover()

urlpatterns = [
    url(r'^', include('openwisp_radius.urls', namespace='freeradius')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
