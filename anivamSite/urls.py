from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='anivamSite'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
