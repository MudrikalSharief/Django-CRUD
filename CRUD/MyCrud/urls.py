from django.urls import path #impoert path from django.urls
from . import views #import views.py from the current directory

urlpatterns = [
    path("", views.index, name="index"), # map the index view to the root URL
]