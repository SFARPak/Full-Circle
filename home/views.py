# pages/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'templates/index.html')

def about(request):
    return render(request, 'templates/about.html')

def blog(request):
    return render(request, 'templates/blog.html')

def blog_details(request):
    return render(request, 'templates/blog_details.html')
def transparency(request):
    return render(request, 'templates/transparency.html')
# app/views.py
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject'] or 'Contact Form Submission'
            message = form.cleaned_data['message']

            full_message = (
                f"You have a new contact form submission:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}"
            )

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECIPIENT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'templates/contact.html', {'form': form})

def elements(request):
    return render(request, 'templates/elements.html')


def events(request):
    videos = [
        {
            'src': 'video1.mp4',
            'poster': 'poster1.jpg',
            'title': 'How they groom'
        },
        {
            'src': 'video2.mp4',
            'poster': 'poster2.jpg',
            'title': 'How they practice'
        },
         {
            'src': 'video3.mp4',
            'poster': 'poster2.jpg',
            'title': 'Physical Exercises'
        },
         {
            'src': 'video.mp4',
            'poster': 'poster2.jpg',
            'title': 'Mental Growth'
        },
        # Add more video entries as needed
    ]
    return render(request, 'templates/events.html', {'videos': videos})

def program(request):
    return render(request, 'templates/program.html')
def support(request):
    return render(request, 'templates/support.html')
def donate(request):
    return render(request, 'templates/donate.html')
