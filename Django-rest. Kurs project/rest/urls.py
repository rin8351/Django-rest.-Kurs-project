from django.contrib import admin
from django.urls import include, path, re_path
from djrest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/kurs/', KursAPIList.as_view()),
    path('api/v1/kurs/<int:pk>/', KursAPIUpdate.as_view()),
    path('api/v1/kursdelete/<int:pk>/', KursAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
