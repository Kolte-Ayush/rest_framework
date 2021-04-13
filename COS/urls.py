from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken import views
from .views import TokenAuth
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('<page>/', views.action),
    # path('stock/', views.stock),
    path('token', TokenAuth.as_view(), name="token"),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
