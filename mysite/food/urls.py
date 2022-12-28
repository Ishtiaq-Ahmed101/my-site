from . import views
from django.urls import path

# Name spacing our app.
app_name = 'food'
###
urlpatterns =  [
    path('',views.index, name= 'index'),
    path('item/', views.items, name= 'items'),
    path('<int:item_id>', views.detail, name='detail'),
    #add items
    path('add/', views.create_item, name='create_item') ,
    # Edit items
    path('update/<int:id>/', views.update_item, name='update_item'),
    # Delete items
    path('delete/<int:id>/', views.delete_item, name= 'delete_item') ,
]