from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('addResume/', views.addResume, name='addresume'),
    path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
