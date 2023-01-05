from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, todoForm
from .models import AppUser
from django.http import HttpResponse

# Create your views here.
def home(request):
    form = todoForm()
    context = {'form': form}
    return render(request, "index.html", context=context)

def login(request):
    forms = UserLoginForm()
    context = {"forms": forms}
    if request.method=="POST":
        request_email = request.POST.get("email")
        request_password = request.POST.get('password')
        
        try:
            user = AppUser.objects.get(email=request_email)
            if user is not None:
                if user.password == request_password:
                    request.session["session_email"] = user.email
                    return redirect("home")

                else:
                    context.setdefault("msg", "Username or password is incorrect !!")
                    return render(request, "login.html", context=context)
            
        except Exception as e:
            return render(request, "login.html", context=context)
    return render(request, "login.html", context=context)


def register(request):
    form = UserRegistrationForm()
    context = {"forms": form}
    if request.method == 'POST':
        user1 = AppUser()
        user1.email = request.POST["email"]
        user1.password = request.POST["password"]
        user1.full_name = request.POST["full_name"]
        user1.contact = request.POST["password"]
        user1.save()
        context.setdefault("msg", "Account created Successfully!!")
    return render(request, "register.html", context=context)

def logout(request):
    if not request.session.has_key("session_email"):
        return redirect("login")
    del request.session["session_email"]
    return redirect("login")