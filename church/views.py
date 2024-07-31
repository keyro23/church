from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView
from django.template.loader import get_template
from .models import Video, Contact, Booking, Event
from .forms import CommercialVideoForm
import datetime

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("Thank you for contacting us")

    # Handle GET request
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


def media_team(request):
    video = Video.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')

        # Save the booking to the database
        booking = Booking(name=name, email=email, service=service, date=date)
        booking.save()

        # Display a success message
        messages.success(request, 'We have received your booking! We will contact you ASAP!')

        # Redirect to avoid resubmission on page refresh
        return redirect('media_team')

    return render(request, 'media_team.html', {"video": video})


def book_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')

        # Save the booking to the database
        booking = Booking(name=name, email=email, service=service, date=date)
        booking.save()

        # Redirect or display a success message
        return redirect('booking_success')  # Replace with your success URL or page

    return render(request, 'booking_form.html')  # Replace with your template name