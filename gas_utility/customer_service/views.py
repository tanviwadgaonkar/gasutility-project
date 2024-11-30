from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm, ServiceRequestUpdateForm

# Home view (Landing page or dashboard)
def home(request):
    return render(request, 'customer_service/home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                next_page = request.GET.get('next', 'home')  # Redirect to next page or home
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill out the form correctly.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            messages.success(request, 'Account created successfully!')
            return redirect('service_requests')  # Redirect to service requests page after signup
    else:
        form = UserCreationForm()

    return render(request, 'customer_service/signup.html', {'form': form})

# Create service request view
@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Assign logged-in user as customer
            service_request.save()
            messages.success(request, 'Your service request has been submitted successfully!')
            return redirect('service_requests')
        else:
            messages.error(request, 'There was an error in your form submission.')
    else:
        form = ServiceRequestForm()

    return render(request, 'customer_service/create_service_request.html', {'form': form})

# Service requests view (Display all service requests)
@login_required
def service_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'customer_service/service_requests.html', {'requests': requests})

# Service request detail view
@login_required
def service_request_detail(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(id=request_id, customer=request.user)
    except ServiceRequest.DoesNotExist:
        messages.error(request, 'Service request not found.')
        return redirect('service_requests')
    
    return render(request, 'customer_service/service_request_detail.html', {'service_request': service_request})

# Update service request view (Only accessible by customer support)
@login_required
def update_service_request(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(id=request_id)
    except ServiceRequest.DoesNotExist:
        messages.error(request, 'Service request not found.')
        return redirect('service_requests')

    # Only allow customer support representatives to update
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to update this request.')
        return redirect('service_requests')

    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request status updated successfully!')
            return redirect('service_request_detail', request_id=request_id)
        else:
            messages.error(request, 'There was an error updating the service request.')
    else:
        form = ServiceRequestUpdateForm(instance=service_request)

    return render(request, 'customer_service/update_service_request.html', {'form': form, 'service_request': service_request})
