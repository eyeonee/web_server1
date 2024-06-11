from django.contrib.auth import authenticate, login as auth_login  # Renamed login to auth_login to avoid conflict
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404  # Added get_object_or_404 for better error handling
from rest_framework import viewsets
from .forms import ContactForm
from .serializers import *
from .models import Contact

# View for listing, adding, editing, and deleting contacts
class ContactListView(viewsets.ModelViewSet):
    "Playground Contact Model"
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

def phonebook(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})  # Updated template name

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phonebook')
    else:
        form = ContactForm()
    return render(request, 'add_persone.html', {'form': form})  # Updated template name

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('phonebook')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_persone.html', {'form': form})  # Updated template name

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('phonebook')
    return render(request, 'delete_persone.html', {'contact': contact})  # Updated template name

# View for managing application information
class AppInfoView(viewsets.ModelViewSet):
    "Playground AppInfo Model"
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer

# View for user login
class LoginView(viewsets.ModelViewSet):
    "Playground Login Model"
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')  # Redirect to the profile page after successful login
        else:
            # Display login credentials error
            pass
    return render(request, 'registration/login.html')

# View for user registration
class RegisterView(viewsets.ModelViewSet):
    "Playground AppInfo Model"
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in user after registration
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View for user profile
class ProfileView(viewsets.ModelViewSet):
    "Playground Profile Model"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('login')  # Redirect to the login page if the user is not authenticated
