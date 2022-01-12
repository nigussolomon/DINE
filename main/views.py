from django.shortcuts import redirect, render

from main.forms import Registration
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request, 'main/home.html')
    
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return redirect('login')
    else:
        form= Registration()
        formLogin=AuthenticationForm()
    return render(request, 'main/register.html',{'form':form})



