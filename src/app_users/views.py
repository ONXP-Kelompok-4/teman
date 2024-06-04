from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ProfileEditForm
# Create your views here.

def profile_view(request):
    profile = request.user.profile
    return render(request, 'app_users/profile.html' , {'profile': profile})

@login_required
def profile_edit_view(request):
    form = ProfileEditForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            # return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
            return redirect('profile')
        else:  
            # form.errors contains the form validation errors  
            return HttpResponse(f'<p class="error">Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}</p>')
    
    return render(request, 'app_users/profile_edit.html', {'form': form})