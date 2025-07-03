from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from . models import student #import the student model from models.py in the current directory
from . forms import AddStudentList #import the AddStudentList form from forms.py in the current directory
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError


@csrf_exempt
# Create your views here.
def index(request):
    return render(request, "home.html")


def showstudents(request):
    list = student.objects.all()  # Get all TodoItem objects from the database
    return render(request, "students_list.html", {"students" : list}) # Render the todo_list.html template with the list of TodoItem objects
def addStudent(request):
    if request.method == "POST":
        form = AddStudentList(request.POST)
        if form.is_valid():
            student.objects.create(**form.cleaned_data)
            return JsonResponse({"success": True, "message": "Student Saved!"})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = AddStudentList()
    return render(request, "create.html", {"form": form})

def get_student(request, student_id):
    try:
        s = student.objects.get(id=student_id)
        data = {
            "id": s.id,
            "name": s.name,
            "course": s.course,
            "year_graduated": s.year_graduated,
            "linkedin_profile": s.linkedin_profile,
            "job_title": s.job_title,
            "company": s.company,
            "start_employment_date": s.start_employment_date.isoformat() if s.start_employment_date else "",
            "end_employment_date": s.end_employment_date.isoformat() if s.end_employment_date else "",
        }
        return JsonResponse({"success": True, "student": data})
    except student.DoesNotExist:
        return JsonResponse({"success": False, "error": "Student not found"})


def update_student(request, student_id):
    if request.method == "POST":
        try:
            s = student.objects.get(id=student_id)
            data = json.loads(request.body)
            s.name = data.get("name", "")
            s.course = data.get("course", "")
            s.year_graduated = data.get("year_graduated", "")
            s.linkedin_profile = data.get("linkedin_profile", "")
            s.job_title = data.get("job_title", "")
            s.company = data.get("company", "")
            s.start_employment_date = data.get("start_employment_date") or None
            s.end_employment_date = data.get("end_employment_date") or None
            try:
                s.full_clean()  # This will validate all fields, including URLField
                s.save()
                return JsonResponse({"success": True})
            except ValidationError as ve:
                # Return validation errors as JSON
                return JsonResponse({"success": False, "errors": ve.message_dict})
        except student.DoesNotExist:
            return JsonResponse({"success": False, "error": "Student not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})

def delete_student(request,student_id):
    if request.method == "POST":
        try:
            Student = student.objects.get(id=student_id)
            Student.delete()
            return JsonResponse({'success':True})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error':'Student not found.'})
        
    return JsonResponse({'success': False, 'error':'Invalid request method.'})