from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . models import TodoItem #import the TodoItem model from models.py in the current directory
from . forms import AddNewList #import the AddNewList form from forms.py in the current directory

# Create your views here.
def index(request):
    return render(request, "home.html")

def show_todo_items(request):
    list = TodoItem.objects.all()  # Get all TodoItem objects from the database
    list = list.order_by("-id")  # Order the TodoItem objects by their ID in descending order
    return render(request, "todo_list.html", {"todos" : list}) # Render the todo_list.html template with the list of TodoItem objects

def create_item(request):
    if request.method == "POST":
        form = AddNewList(request.POST)  # Create an instance of the AddNewList form

        if form.is_valid():
            title = form.cleaned_data["todo_name"]  # Get the cleaned data from the form\
            list = TodoItem(title=title)
            list.save()  # Save the new TodoItem to the database

            return HttpResponse("Item added successfully!\n Item : " + list.title + "\n<a href='/create/'>Go back to the list</a>")  # Return a success message with a link to the todo list
    else:
        form = AddNewList()
                    
    return render(request, "create.html", {"form" : form})  # Render the create.html template for creating a new TodoItem