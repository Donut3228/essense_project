from django.urls import path
from objects_manager import views


urlpatterns = [
    path('om_index/', views.index, name='om_index'),
]