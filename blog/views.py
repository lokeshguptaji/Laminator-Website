from django.shortcuts import render,redirect,HttpResponse
from .models import Post,BlogComment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def blogHome(request):
    posts=Post.objects.all()
    return render(request,'blog/blogHome.html',{'posts':posts})

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post)
    return render(request,'blog/blogPost.html',{'post':post,'comments':comments})


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)

        fcomment=BlogComment(comment=comment,user=user,post=post)
        fcomment.save()
        messages.success(request,"you commented successfully")
    return redirect(f"/blog/{post.slug}")

def handleSignUp(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #checks for error
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('/blog')
        if not username.isalnum():
            messages.error(request,"Username should only contain letters")
            return redirect('/blog')
        if pass1!=pass2:
            messages.error(request,"Your passwords are not matched.")
            return redirect('/blog')
        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Congartulations,You have successfully created a User")
        return redirect('/blog')
    
def handleLogin(request):
    if request.method=='POST':
        loginUsername=request.POST['loginUsername']
        loginPassword=request.POST['loginPassword']

        user=authenticate(username=loginUsername,password=loginPassword)
        if user is not None:
            login(request,user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('/blog')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/blog')
    return HttpResponse("Login")

def handleLogout(request):
        logout(request)
        messages.success(request,"Successfully Logout")
        return redirect("/blog")
