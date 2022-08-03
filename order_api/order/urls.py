from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('list/', views.order_list, name="list"),
    path('create/', views.order_create, name="create"),
    path('detail/<int:pk>', views.order_detail, name="detail"),
    # path('create/', views.order_list_published, name="create"),
]