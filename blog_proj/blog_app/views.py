from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def add_view(request):
    form = BlogModelForm()
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show")
    return render(request,"blog/add.html",{"form":form})

def show_view(request):
    obj = Blog.objects.all()
    if request.method == 'GET':
        s = request.GET.get('search')
        if s:
            obj =Blog.objects.filter(title__contains=s)

    return render(request,"blog/show.html",{"obj":obj})
@login_required(login_url="/login")
def update_view(request,i):
    b = Blog.objects.get(id=i)
    form = BlogModelForm(instance=b)
    if request.method == 'POST':
        form = BlogModelForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return redirect("/show")
    return render(request, "blog/add.html", {"form": form})
@login_required(login_url="/login")
def delete_view(request,i):
    obj = Blog.objects.get(id=i)
    if request.method == 'POST':
        obj.delete()
        return redirect("/show")
    return render(request,"blog/delete.html",{"obj":obj})

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    return render(request,"blog/register.html",{"form":form})

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('ps')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("/show")

    return render(request,"blog/login.html",{})

def logout_view(request):
    logout(request)
    return redirect("/login")