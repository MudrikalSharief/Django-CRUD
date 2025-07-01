from django.urls import path #impoert path from django.urls
from . import views #import views.py from the current directory


urlpatterns = [
    path("", views.index, name="index"), # map the index view to the root URL
    path("todo/", views.show_todo_items, name="show_todo_items"), # map the show_todo_items view to the /todo/ URL
]