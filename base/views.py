from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # Obtain the username and password of the user trying to login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # Now check if the username and password are correct
        user = authenticate(request, username=username, password=password)

        # If everything correct, login the user then redirect them to the home page
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context= {}
    return render(request, 'base/login_register.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    query = request.GET.get('query') if request.GET.get('query') != None else ''
    rooms = Room.objects.all().filter(Q(topic__name__icontains=query) |
                                      Q(name__icontains=query) | 
                                      Q(description__icontains=query)
                                      )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context=context)

@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room})