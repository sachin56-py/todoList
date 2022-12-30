from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import AppUser

# Create your views here.
def home(request):
    return render(request, "index.html")

def login(request):
    forms = UserLoginForm()
    context = {"forms": forms}
    if request.method=="POST":
        request_email = request.POST.get("email")
        request_password = request.POST.get('password')
        user = AppUser.objects.get(email=request_email)
        if user.password == request_password:
            request.session["session_email"] = user.email
            return redirect("home")
        else:
            context.setdefault("msg", "Username or password is incorrect !!")
            return render(request, "login.html", context=context)
        # req_email = request.POST.get("email")
        # req_password = request.POST.get("password")
        # user = AppUser.objects.get(email=req_email)
        # if user.email==req_email and user.password==req_password:
        #     request.session["session_email"] = user.email
        #     # this code can also be written as
        #     # 2) -> request.session.setdefault("session_email", user.email)
        #     # 3) -> request.session.update({"session_email": user.email})
        #     return redirect("home")
        # else:
        #     return redirect("login")
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