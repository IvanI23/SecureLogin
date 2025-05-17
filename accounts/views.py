from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .utilities import send_verification_email, password_reset_email, generate_verification_code
from .models import UserProfile 
from django.contrib.auth.decorators import login_required


# views.py
def home(request):
    context = {}
    if request.user.is_authenticated:
        try:
            context['profile'] = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass
    return render(request, 'accounts/home.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home or dashboard
        else:
            return render(request, "accounts/login.html", {"login_failed": True})  # Pass login_failed=True

    return render(request, "accounts/login.html", {"login_failed": False})

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'register_failed': True})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Generate verification code and create profile
        verification_code = generate_verification_code()
        UserProfile.objects.create(user=user, verification_code=verification_code, email_verified=False)
        
        # Send verification email
        send_verification_email(user.email, verification_code)
        
        return redirect('verify_email')

    return render(request, 'accounts/register.html', {'register_failed': False})

def logout_user(request):
    logout(request)
    return redirect('home')

def verify_email(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        try:
            profile = UserProfile.objects.get(verification_code=entered_code)
            if not profile.email_verified:
                profile.email_verified = True
                profile.save() 
                return render(request, 'accounts/verify_email.html', {'verification_success': True})
            return render(request, 'accounts/verify_email.html', {'verification_failed': True, 'error': 'Email already verified'})
        except UserProfile.DoesNotExist:
            return render(request, 'accounts/verify_email.html', {'verification_failed': True, 'error': 'Invalid verification code'})
    return render(request, 'accounts/verify_email.html')

def reverify(request):
    verification_code = generate_verification_code()
    profile = UserProfile.objects.get(user=request.user)  

    profile.verification_code = verification_code  
    profile.save() 
    
    send_verification_email(request.user.email, verification_code)
    return redirect('verify_email')
    
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            verification_code = generate_verification_code()
            profile = UserProfile.objects.get(user=user)
            profile.verification_code = verification_code
            profile.save()
            password_reset_email(email, verification_code)
            return render(request, 'accounts/final_reset.html')
        except User.DoesNotExist:
            pass
    return render(request, 'accounts/reset_password.html')

def final_reset(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        email = request.POST.get('email')
        password = request.POST.get('new_password')
        try:
            profile = UserProfile.objects.get(verification_code=entered_code)
            if profile.user.email == email:
                user = profile.user
                user.set_password(password)
                user.save()
                if not profile.email_verified:
                    profile.email_verified = True
                    profile.save() 
                return redirect('login')
        except UserProfile.DoesNotExist:
            return render(request, 'accounts/final_reset.html', {'verification_failed': True})
    return render(request, 'accounts/final_reset.html')
