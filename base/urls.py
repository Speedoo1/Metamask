from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [

    path('', views.index, name="name"),
    path('wallet/', views.connector, name='tok'),
     path('success/', views.success, name='suc')
]
