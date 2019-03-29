from django.urls import path
from rest_framework.authtoken import views
from appi.views import ProductoList, ProductoDetalle, UserCreate
 
urlpatterns = [
    path('v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>/', ProductoDetalle.as_view(),name='producto_detalle' ),
    path('v1/users/', UserCreate.as_view(), name='users_create'),
    path('v1/login/', views.obtain_auth_token, name='login'),

]