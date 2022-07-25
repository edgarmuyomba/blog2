from django.urls import path 
from . import views
from django.conf.urls.static import static 
from blog.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT

app_name = 'authentication'

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView, name='logout'),
    path('signup/', views.SignUpPageView.as_view(), name='signup'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)