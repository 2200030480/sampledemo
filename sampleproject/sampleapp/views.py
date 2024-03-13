from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def addStudent(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        course = request.POST.get('course')
        fees = request.POST.get('fees')

        # Create a new Student instance and save it
        st = Student(sname=sname, course=course, fees=fees)
        st.save()

        # Return a response indicating that the student has been added successfully
        return render(request, 'add_student.html', {'saved': True})

    # If request method is not POST, render the add_student.html template
    return render(request, 'add_student.html')
