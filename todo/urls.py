from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page, name = "main_page"),
    path('addTodo/', views.addTodo, name = "addTodopage"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name = "deleteTodopage"),
]