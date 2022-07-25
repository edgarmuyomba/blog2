from django.urls import path 
from . import views
from django.conf.urls.static import static 
from blog.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:uuid>/', views.details, name='details'),
    path('new_post/', views.new_post, name='new_post'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)