from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  SignUpForm, AddCustomerForm
from .models import Customer



def home(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have Been Login...")
        else:
            messages.success(request, "There Was An Error. Try Again...")
            return redirect ('home')
    return render(request, 'home.html', {'customers': customers})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logout...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Registered Successfully. Welcome!")
            return redirect ('home')
    else:
        form = SignUpForm()
        return render(request, 'register_user.html', {'form': form})
    return render(request, 'register_user.html', {'form': form})


def customer_data(request, pk):
    if request.user.is_authenticated:
        customer_data = Customer.objects.get(id=pk)
        return render(request, 'customer_data.html', {'customer_data': customer_data})
    else:
        messages.success(request, "You Must Be Login To See That Page...")
        return redirect ('home')


def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Login To Do That...")
        return redirect('home')


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Customer Added Successfully...")
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, "You Must Be Login To Do That...")
        return redirect('home')


def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Data Updated Successfully!")
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, "You Must Be Login To Do That...")
        return redirect('home')