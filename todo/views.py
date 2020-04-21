from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo

# Create your views here.

def main_page(request):
    all_todo_items = todo.objects.all()
    return render(request, "todo.html",
                  {"all_items" : all_todo_items})

def addTodo(request):
    new_item = todo(content = request.POST['content'])
    new_item.save()

    return redirect('/todo/main/')

def deleteTodo(request, todo_id):
    item_to_delete = todo.objects.get(id=todo_id)
    item_to_delete.delete()

    return redirect('/todo/main/')
