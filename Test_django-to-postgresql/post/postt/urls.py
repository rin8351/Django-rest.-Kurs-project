from django.urls import path
from . import views

urlpatterns=[
    path('', views.kurs_f, name='kurs'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:pk>/update', views.update_row.as_view(), name='update_row'),
    path('<int:pk>/delete', views.delete_row.as_view(), name='delete_row'),
]
