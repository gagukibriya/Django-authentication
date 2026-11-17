from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# success page view

@login_required
def success_view(request):
    return render(
        request,
        template_name='successful.html'
    )


## Register page view

def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            return render (
                request,
                'register.html',
                {'error': 'Username alrady exists!'}
            )

        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        return redirect('/login/')

    return render(
        request,
        template_name='register.html'

    )


### Login View

def login_view(request):

    if request.method == 'POST':

        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(
            email = username_or_email
        ).first()

        if user is None:
            user = User.objects.filter(
                username = username_or_email
            ).first()

        if user is not None:
            authenticate_user = authenticate(
                request,
                username = user.username,
                password = password
            )

            if authenticate_user is not None:
                login(
                    request,
                    authenticate_user
                )
                return redirect('success')

        return render(
            request,
            'login.html',
            {'error': 'Invalid username/email or password!'}
        )

    return render (
        request,
        template_name='login.html'
    )




#### Log Out View

def logout_view(request):
    logout (request)
    return redirect('login')