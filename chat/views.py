from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'chat/login.html')

def chat(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        return render(request, 'chat/chat.html', {
            'username': username,
            'room': room
        })
    return redirect('index')
