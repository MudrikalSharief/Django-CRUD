from django.shortcuts import render, HttpResponse
from . models import TodoItem #import the TodoItem model from models.py in the current directory

# Create your views here.
def index(request):
    return render(request, "home.html")

def show_todo_items(request):
    list = TodoItem.objects.all()  # Get all TodoItem objects from the database
    return render(request, "todo_list.html", {"todos" : list}) # Render the todo_list.html template with the list of TodoItem objects