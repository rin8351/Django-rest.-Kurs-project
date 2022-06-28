from django.urls import path
from . import views

urlpatterns=[
    path('', views.kurs_f, name='kurs'),
    path('<int:pk>/update', views.update_row.as_view(), name='update_row'),
    path('<int:pk>/delete', views.delete_row.as_view(), name='delete_row'),
]