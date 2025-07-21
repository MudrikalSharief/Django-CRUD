from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
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
    # Get search query from URL
    query = request.GET.get('search', '')
    
    # Start with all students
    student_list = student.objects.all()
    
    # Filter by search query if it exists
    if query:
        student_list = student_list.filter(
            # Search in multiple fields
            Q(name__icontains=query) |
            Q(course__icontains=query) |
            Q(company__icontains=query) |
            Q(job_title__icontains=query)
        )
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(student_list, 10)  # Show 10 students per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Add pagination info
    context = {
        "students": page_obj,
        "search_query": query,
        "total_students": student_list.count(),
        "paginator": paginator
    }
    
    return render(request, "students_list.html", context)

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