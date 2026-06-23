from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Appointment, Department

# Create your views here.

def home(request):
    departments = Department.objects.all()
    return render(request, "home.html", {
        "departments": departments
    })

def about(request):
    return render(request, "about.html")

def doctors(request):
    return render(request, "doctors.html")

def departments(request):
    return render(request, "departments.html")

def contact(request):
    return render(request, "contact.html")

def appointment(request):
    departments = Department.objects.all()

    if request.method == "POST":
        patient_name = request.POST.get('patient_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        department_id = request.POST.get('department', '').strip()
        appointment_date = request.POST.get('appointment_date', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not patient_name or not phone or not appointment_date:
            messages.error(request, "Please fill in all required appointment fields.")
            return render(request, "appointment.html", {
                "departments": departments,
                "patient_name": patient_name,
                "phone": phone,
                "appointment_date": appointment_date,
                "message": message_text,
                "selected_department": department_id
            })

        department = None
        if departments.exists() and not department_id:
            messages.error(request, "Please select a valid department.")
            return render(request, "appointment.html", {
                "departments": departments,
                "patient_name": patient_name,
                "phone": phone,
                "appointment_date": appointment_date,
                "message": message_text,
                "selected_department": department_id
            })

        if department_id:
            try:
                department = Department.objects.get(pk=department_id)
            except Department.DoesNotExist:
                messages.error(request, "Selected department is invalid.")
                return render(request, "appointment.html", {
                    "departments": departments,
                    "patient_name": patient_name,
                    "phone": phone,
                    "appointment_date": appointment_date,
                    "message": message_text,
                    "selected_department": department_id
                })

        try:
            Appointment.objects.create(
                patient_name=patient_name,
                phone=phone,
                department=department,
                appointment_date=appointment_date,
                message=message_text
            )
            messages.success(request, "Appointment Booked Successfully!")
            return render(request, "appointmentsuccess.html")
        except Exception as e:
            messages.error(request, f"Unable to save appointment: {e}")
            return render(request, "appointment.html", {
                "departments": departments,
                "patient_name": patient_name,
                "phone": phone,
                "appointment_date": appointment_date,
                "message": message_text,
                "selected_department": department_id
            })

    return render(request, "appointment.html", {
        "departments": departments
    })

def login(request):
    return render(request, "login.html")