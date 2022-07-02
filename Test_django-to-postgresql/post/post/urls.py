from django.contrib import admin
from django.urls import path
from django.urls import include
from postt.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postt.urls')),
]

handler404=pageNotFound
