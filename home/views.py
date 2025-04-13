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

def contact(request):
    return render(request, 'templates/contact.html')

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
