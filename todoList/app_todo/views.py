from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, todoForm
from .models import AppUser, todo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    if not request.session.has_key("session_email"):
        return redirect("login")
    form = todoForm()
    context = {'form': form}
    if request.method == "POST":
        todos = todo()
        todos.title = request.POST.get('title')
        todos.details = request.POST.get('title')
        todos.status = request.POST.get('status')
        todos.date = request.POST.get('date')
        todos.priority = request.POST.get('priority')
        todos.save()
        return redirect("home")
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

# def todo_show(request):
#     if request.session.has_key("session_email"):
#         user = request.user
#         print(user)
#         data = todo.objects.get()
#         context = {"data": data}
#         return render(request, "index.html", context)
#     else:
#         return redirect("register")
