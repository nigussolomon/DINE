from django.shortcuts import redirect, render

from main.forms import Registration

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return redirect('login')
    else:
        form= Registration()
    return render(request, 'main/register.html')

