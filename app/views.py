from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


from .forms import SignupForm


def home(request):
    return render(request, 'home.html')  # Ensure this template exists



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
  
  
 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home URL pattern
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')




# login page
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# logout page
# def user_logout(request):
#     logout(request)
#     return redirect('login')
def user_logout(request):
    logout(request)
    return redirect('core:login')  # Use the namespace if applicable
