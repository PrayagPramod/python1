from django.urls import path

from travelapp import views
from travelproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.demo, name='demo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
