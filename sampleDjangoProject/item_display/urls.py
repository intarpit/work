from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

app_name = 'washBasin'
urlpatterns = [
    path('', views.item_display, name='item'),
    path('detail/', views.item_detail, name='item_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)