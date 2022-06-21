from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from neighborhood.forms import *
from django.contrib import messages
from neighborhood.models import *
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    b_form = CreateBusinessForm()
    h_form = HoodCreationForm()
    context = {
        'b_form': b_form,
        'h_form': h_form
    }
    return render(request, 'neighborhood/index.html', context)


@login_required
def create_business(request):
    b_form = CreateBusinessForm()
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        b_form = CreateBusinessForm(request.POST)
        if b_form.is_valid():
            new_business = Business.objects.create(
                user = current_user, 
                hood = current_user.profile.hood, 
                business_name = request.POST.get('business_name'),
                email = request.POST.get('email')
            )
            new_business.save()
            messages.success(request, 'Success! You new business has been created!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! Your new business could not be created!')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home', )



@login_required
def create_hood(request):
    h_form = HoodCreationForm()
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        h_form = HoodCreationForm(request.POST)
        if h_form.is_valid():
            new_hood = Neighborhood.objects.create(
                hood_name = request.POST.get('hood_name'),
                location = request.POST.get('location'),
                admin = current_user
            )
            new_hood.save()
            messages.success(request, 'Success! You have created a new hood!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! The new hood could not be created')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home')
        
