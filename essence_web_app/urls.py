from django.urls import path, include

from essence_web_app import views
from django.urls.exceptions import NoReverseMatch


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('checkout/', views.checkout, name='checkout'),
]
