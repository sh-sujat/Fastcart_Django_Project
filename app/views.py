from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *


def index(request):
    category = Category.objects.all()
    cat_id = request.GET.get('cata')
    search = request.GET.get('search')
    if search:
        products = Products.objects.filter(name__icontains=search)
    else:
        if cat_id:
            products = Products.objects.filter(category=cat_id)
        else:
            products = Products.objects.all()
    return render(request, 'index.html', locals())


def registration(request):
    category = Category.objects.all()
    if request.user.is_active:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This username is already taken, try another')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'This email is already taken, try another')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, 'Profile created, login now')
                return redirect('login')
        else:
            messages.warning(request, 'Miss match password')
            return redirect('registration')
    else:
        return render(request, 'registration.html', locals())


def login(request):
    category = Category.objects.all()
    if request.user.is_active:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'User not found, create an account')
            return redirect('registration')
    else:
        return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required
def profile(request):
    category = Category.objects.all()
    picture = ProfilePic.objects.all()
    return render(request, 'profile.html', locals())


def prod(request, id):
    pro = Products.objects.filter(id=id)
    category = Category.objects.all()
    return render(request, 'product.html', locals())


def review(request):
    return render(request, 'review.html', locals())
