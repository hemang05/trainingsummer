from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.forms import Signup
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_view(request):
    return render(request,'testapp/java.html')

def logout_view(request):
    return render(request,'testapp/logout.html')


def signupview(request):
    form=Signup()
    if request.method=="POST":
        form=Signup(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})
