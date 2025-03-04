from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    #  Books
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # Adding Books
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # Edit Books
    path('update/<int:id>/', views.update_item, name='update_item'),
    # Delete Books
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]