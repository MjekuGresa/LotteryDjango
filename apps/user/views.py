from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "user/index.html")

def login_page(request):
    return render(request, "user/login.html")

def register_page(request):
   return render(request, "user/register.html")

def create(request):
   errors = User.objects.validate(request.POST)
   if errors:
      for error in errors:
         messages.error(request, error)
      return redirect('user:login')
   user_id = User.objects.create_user(request.POST)
   request.session['user_id'] = user_id
   request.session['input'] = 'register'
   return redirect('ticket:index')

def login(request):
   valid, result = User.objects.login(request.POST)
   if not valid:
      messages.error(request, result)
      return redirect('user:index')
   request.session['user_id'] = result
   request.session['input'] = 'login'
   return redirect('ticket:index')

def logout(request):
   request.session.clear()
   return redirect('user:index')

def edit(request):
   context = {'user': User.objects.get(id=request.session['user_id'])}
   return render(request, "user/edit.html", context)

def update(request):
   if request.method == 'POST':
      errors = User.objects.basic_validator(request.POST)
      if errors:
         for error in errors:
            messages.error(request, error)
         return redirect('user:edit')
      else:
         User.objects.change_password(request.POST['password'], request.session['user_id'])
         return redirect('ticket:index')
