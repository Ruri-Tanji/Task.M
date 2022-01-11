from django.urls import path
from . import views

urlpatterns = [
    #ToDo
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_list_id>', views.update, name='update'),
    path('delete/<int:todo_list_id>', views.delete, name='delete'),
    
    #Memo
    path('memo/', views.memo, name='memo'),
    path('memo/create/', views.memo_create, name='memo_create'),
    path('memo/delete/<int:memo_list_id>', views.memo_delete, name='memo_delete'),
    path('hand/', views.hand, name='hand'),
]