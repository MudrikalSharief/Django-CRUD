from django import forms

class AddStudentList(forms.Form):

    name = forms.CharField(label="Student Full Name  ", max_length=200)
    course = forms.CharField(label="Course  ", max_length=200)
    year_graduated = forms.IntegerField(label="Year Graduated  ")
    linkedin_profile = forms.URLField(label="Linkedin Url  ", required=False)
    job_title = forms.CharField(label="Job Title  ", max_length=200, required=False)
    company = forms.CharField(label="Company  ", max_length=200, required=False)
    start_employment_date = forms.DateField(label="Employment Date  ", required=False)
    end_employment_date = forms.DateField(label=" End Date  ", required=False)