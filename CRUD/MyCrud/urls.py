from django.urls import path #impoert path from django.urls
from . import views #import views.py from the current directory


urlpatterns = [
    path("", views.index, name="index"), # map the index view to the root URL
    path("students/", views.showstudents, name="showstudents"), # map the showstudents view to the /students/ URL
    path("students/add/", views.addStudent, name="addstudent"), # map the add student view to the /students/add/ URL
    path("student/delete/<int:student_id>/", views.delete_student, name="deletestudent"),
    path("student/get/<int:student_id>/", views.get_student, name="getstudent"),
    path("student/update/<int:student_id>/", views.update_student, name="updatestudent"),
]