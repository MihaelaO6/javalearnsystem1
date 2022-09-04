from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html')
def materials(request):
    return render(request, 'materials.html')
def quizz(request):
    return render(request, 'quizz.html')
def reminder(request):
    return render(request, 'reminder.html')
def sertificate(request):
    return render(request, 'sertificate.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')