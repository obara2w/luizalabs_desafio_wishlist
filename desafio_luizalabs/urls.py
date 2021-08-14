from django.contrib import admin
from django.urls import include, path
from django.views import generic
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', generic.RedirectView.as_view(pattern_name='api-root')),
    path('api/', include(router.urls)),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
