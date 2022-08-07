from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('create/', views.order_create, name="create"),
    path('list/', views.order_list, name="list"),
    path('detail/<int:pk>', views.order_detail, name="detail"),
    path('update/<int:pk>', views.order_update, name="update"),
    path('delete/<int:pk>', views.order_delete, name="delete"),
    # path('create/', views.order_list_published, name="create"),
]