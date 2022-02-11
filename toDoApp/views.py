from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as l,logout as lo,authenticate
from .forms import ToDoForm as form
from django.utils  import   timezone
from .models import ToDo
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST["password1"], )
                user.save()
                l(request,user)
                return redirect('currentToDo')
            except IntegrityError:
                return render(request, 'todo/signup.html', {'form': UserCreationForm(),"error": 'Username already taken: Please Chose a different username '})

        else:
            return render(request, 'todo/signup.html', {'form': UserCreationForm(),"error": 'Passwords did not match'})


def login(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', {'form': AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html', {'form': AuthenticationForm(),'error':'Username and password did not match'})
        else:
            l(request,user)
            return redirect('currentToDo')

                           
@login_required 
def logout(request):
    if request.method=='POST':
        lo(request)
        return redirect('home')
@login_required
def createToDo(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html', {'form': form()})
    else:
        try:
            f=form(request.POST)
            f.save(commit=False).user = request.user
            toDo= f.save(commit=False)
            toDo.save()
            return redirect('currentToDo')
        except ValueError:
            return render(request, 'todo/create.html', {'form': form()},'Error:Invalid Data. Please try again')
@login_required
def currentToDo(request):
    list=ToDo.objects.filter(user=request.user,date__isnull=True).order_by('-important','-created')
    return render(request,'todo/current.html',{'list':list})
@login_required
def completedToDo(request):
    list=ToDo.objects.filter(user=request.user,date__isnull=False).order_by('date')
    return render(request,'todo/completed.html',{'list':list})
@login_required
def completeToDo(request, todo_pk):
   toDo=get_object_or_404(ToDo,pk=todo_pk,user=request.user)
   if  request.method =='POST':
       toDo.date=timezone.now()
       toDo.save()
       return redirect('currentToDo')
@login_required
def deleteToDo(request, todo_pk):
   toDo=get_object_or_404(ToDo,pk=todo_pk,user=request.user)
   if  request.method =='POST':
       toDo.delete()
       return redirect('completeToDo')
@login_required
def reverseToDo(request, todo_pk):
    toDo=get_object_or_404(ToDo,pk=todo_pk,user=request.user)
    if  request.method =='POST':
        toDo.date= None
        toDo.save()
        return redirect('currentToDo')

@login_required
def viewToDo(request, todo_pk):
    toDo=get_object_or_404(ToDo,pk=todo_pk,user=request.user)
    if request.method =='GET':
        f=form(instance= toDo)
        return render(request,'todo/todo.html',{'toDo':toDo,'form':f})
    else:
        try:
            f=form(request.POST,instance=toDo)
            f.save()
            return redirect('currentToDo')
        except ValueError:
            return render(request, 'todo/todo.html', {'toDo':toDo,'form': f,'error':'Invalid Data. Please try again'})

        