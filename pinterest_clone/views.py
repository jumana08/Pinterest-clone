from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from .models import *
import random

def username_initial_function(request):
    current_user=request.user.username
    current_user=str(current_user)
    
    if(current_user[0].islower()):
        user_initial=current_user[0].capitalize()
    else:
        user_initial=current_user[0]

    return user_initial

def index(request):
    return render(request,"index.html")

def home(request):
    current_user=request.user.username
    images=[]
    images1=[]
    i2=[]
    interests=Interest.objects.filter(username=current_user)
    for i in interests:
        images += Image.objects.filter(category=i.interest)
        i2.append(i.interest) 
    
    i1 = ['makeup', 'art', 'henna', 'nature', 'recipes', 
    'friendship', 'beauty_products', 'flowers', 'hairstyles', 'babies', 
    'child', 'sketching', 'travel', 'yoga', 'nails', 
    'birthday', 'disney', 'dress', 'birds', 'jewellery', 
    'quotes', 'drawing', 'love', 'shoes', 'morning','other']

    remaining = list(set(i1) - set(i2)) + list(set(i2) - set(i1))

    for i in remaining:
        images1 += Image.objects.filter(category=i)

    user_initial = username_initial_function(request)
    
    images = random.sample(images, len(images))
    images1 = random.sample(images1, len(images1))
    params = {'images': images , 'user_initial':user_initial , 'images1':images1}
    return render(request,"home.html" , params)

def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        dob=request.POST['dob']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! , Please try again with another one.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email address already exists! , Please login using this email address or reset the password.")
            return redirect('index')

        myuser = User.objects.create_user(username, email, password)
        myuser.dob = dob
        myuser.save()
        myuser2 = user1(username=username)
        myuser2.save()
        user=authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
        messages.success(request, "Account Created Successfully.")
        return render(request , "interest.html")
        # return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in Successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again.")
            return redirect('index')


    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

def interest(request):
    if request.method=="POST":
        current_user=request.user.username
        user=user1.objects.get(username=current_user)
        values=request.POST['textbox']
        values=values.split(',')
        l=len(values)
        if(values[l-1]==values[l-2]):
            values.pop(l-1)
        print(values)
        for i in values:
            record=Interest(username=user, interest=i)
            record.save()
        return redirect('home')

    return HttpResponse("404- Not found")

def ReachUs(request):
    return render(request,"about.html")

def feedback(request):
    feedback=request.POST['feedback']
    print(feedback)
    messages.success(request, "Thank you for your valuable feedback!")
    return render(request,"about.html")


def profile(request):

    user_initial=username_initial_function(request)
    current_user=request.user.username
    user_details=User.objects.get(username=current_user)

    params={'user_initial':user_initial , 'user_details':user_details}
    return render(request,"profile.html" , params)

def liked(request):
    images=[]
    current_user=request.user.username
    liked_images=Like.objects.filter(username=current_user)

    for i in liked_images:
        temp=Image.objects.get(image_id=i.image_id.image_id)
        images.append(temp)

    user_initial=username_initial_function(request)
    params={'user_initial':user_initial , 'images':images}
    return render(request , "liked.html",params)

def saved(request):
    images=[]
    current_user=request.user.username
    saved_images=Save.objects.filter(username=current_user)

    for i in saved_images:
        temp=Image.objects.get(image_id=i.image_id.image_id)
        images.append(temp)

    user_initial=username_initial_function(request)
    params={'user_initial':user_initial , 'images':images}
    return render(request , "saved.html",params)

def uploaded(request):
    images=[]
    current_user=request.user.username
    uploaded_images=Image.objects.filter(username=current_user)

    user_initial=username_initial_function(request)
    params={'user_initial':user_initial , 'images':uploaded_images}
    return render(request , "uploaded.html",params)


def image_view(request , id):
    image=Image.objects.get(image_id = id)
    user_initial=username_initial_function(request)
    current_user=request.user.username
    user=user1.objects.get(username=current_user)
    if Like.objects.filter(username=user , image_id=image).exists():
        x=1
    else:
        x=0

    if Save.objects.filter(username=user , image_id=image).exists():
        status='Saved'
    else:
        status='Save'

    like=Like.objects.filter(image_id = image)
    like=len(like)
    params={'image':image , 'user_initial':user_initial , 'like':like , 'x':x, 'status':status}
    return render(request , "image_view.html" , params)

def liking(request , id):
    image=Image.objects.get(image_id = id)
    current_user=request.user.username
    user=user1.objects.get(username=current_user)
    user_initial = username_initial_function(request)
    if Like.objects.filter(username=user , image_id=image).exists():
        l=Like.objects.get(username=user , image_id=image)
        l.delete()
        x=0
    else:
        l=Like(username=user , image_id=image)
        l.save()
        x=1

    total_like = Like.objects.filter(image_id = image)
    total_like=len(total_like)

    params={'user_initial':user_initial , 'like':total_like,'image':image , 'x':x}
    return redirect('image_view' , id)

def saving(request , id):
    status=""
    image=Image.objects.get(image_id = id)
    current_user=request.user.username
    user=user1.objects.get(username=current_user)
    user_initial = username_initial_function(request)
    if Save.objects.filter(username=user , image_id=image).exists():
        l=Save.objects.get(username=user , image_id=image)
        l.delete()
        status="Save"
    else:
        l=Save(username=user , image_id=image)
        l.save()
        status="Saved"

    params={'user_initial':user_initial , 'status':status,'image':image}
    return redirect('image_view' , id)


def upload_page(request):
    return render(request, "upload_form.html")

def uploading(request):
    current_user = request.user.username
    user=user1.objects.get(username=current_user)
    title = request.POST['title']
    description = request.POST['description']
    category = request.POST['category']
    image = request.FILES['image']
    i=Image(username=user , image=image , title=title , description=description, category=category)
    i.save()
    messages.success(request, "Image Uploaded Successfully.")
    return render(request , "upload_form.html")

def Settings(request):
    current_user=request.user.username
    user=User.objects.get(username=current_user)
    user_initial = username_initial_function(request)
    params={'user_initial':user_initial , 'user':user}
    return render(request, "settings.html" , params)
    
    
def update_profile(request):
    current_user=request.user.username
    user=User.objects.get(username=current_user)

    new_username=request.POST['username']
    new_email=request.POST['email']

    if(new_username == user.username and new_email==user.email):
        return redirect('Settings')

    if(new_username == user.username and new_email!=user.email):
        user.email=new_email
        user.save()
        messages.success(request, "Profile Uploaded Successfully.")
        return redirect('Settings')

    user.username=new_username
    user.email=new_email
    user.save()
    messages.success(request, "Profile Uploaded Successfully.")
    return redirect('Settings')

def change_password(request):
    return render(request , "reset_password.html")

def home_searching(request , category):
    images=Image.objects.filter(category=category)
    return render(request , "search.html" , {"images":images , "category":category})
    
def liked_searching(request , category):
    images=[]
    liked_images=Like.objects.filter(username=request.user.username)
    for i in liked_images:
        if Image.objects.filter(category=category , image_id=i.image_id.image_id).exists():
            temp=Image.objects.get(category=category , image_id=i.image_id.image_id)
            images.append(temp)
    return render(request , "search.html" , {"images":images , "category":category})

def saved_searching(request , category):
    images=[]
    saved_images=Save.objects.filter(username=request.user.username)
    for i in saved_images:
        if Image.objects.filter(category=category , image_id=i.image_id.image_id).exists():
            temp=Image.objects.get(category=category , image_id=i.image_id.image_id)
            images.append(temp)
    return render(request , "search.html" , {"images":images , "category":category})

def uploaded_searching(request , category):
    images=Image.objects.filter(category=category , username=request.user.username)
    return render(request , "search.html" , {"images":images , "category":category})


def user_profile(request , username):
    images=Image.objects.filter(username=username)

    current_user=username
    current_user=str(current_user)
    
    if(current_user[0].islower()):
        user_initial=current_user[0].capitalize()
    else:
        user_initial=current_user[0]

    user_details=User.objects.get(username=username)
    params={'user_initial':user_initial , 'user_details':user_details , 'images':images}
    return render(request , "user_profile.html" , params)
