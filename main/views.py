from django.shortcuts import redirect, render

from main.forms import Registration
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        formLogin= AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return redirect('login')
        elif formLogin.is_valid():
            formLogin.save()
            formLogin.cleaned_data
            
    else:
        form= Registration()
        formLogin=AuthenticationForm()
    return render(request, 'main/home.html',{'form':form})



