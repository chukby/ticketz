from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterClientForm


# Register a client.
def register_client(request):
    if request.method == 'POST':
        form = RegisterClientForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.is_client = True
            username = temp.cleaned_data.get('username')
            temp.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.warning(request,
                             'Something went wrong, invalid form inputs!')
    else:
        form = RegisterClientForm()
        context = {'form': form}
    return render(request, 'users/register_client.html', context)


# Login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Login successful, Welcome {username}!')
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Something went wrong, Invalid username or password!')
            return redirect('login')
    return render(request, 'users/login.html')


# Logout a user
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')
