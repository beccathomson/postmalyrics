from django.shortcuts import render
from django import forms

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if not form.is_valid():
            print (form.errors)
            return render(request, 'signup.html', {'form': form})
        else:
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(email=email,
                                                password=password,
                                                     )
            new_user.is_active = True
            new_user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})    