from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'', include('apps.core.urls', namespace='core')),
    url(r'^product/', include('apps.product.urls', namespace='product')),
    
    url(r'^groupproduct/', include('apps.group_product.urls', namespace='group_product')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

