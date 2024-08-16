from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_user,name="register_user"),
    path("login/", views.login_user,name="login_user"),
    path('profile/', views.ProfileView,name="profile"),
    path('products/',views.products_list,name='products'),
    path('products/<int:pk>/',views.products_detail,name='products_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)