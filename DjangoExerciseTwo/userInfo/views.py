from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from userInfo.models import User
from django.contrib.auth.models import User as User_default

from . import forms

#for login
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    index_dict = {'insert_index':"Go to /users to see the list of user information, /forms to fill the form"}
    return render(request,'userInfo/index.html',context=index_dict)

def users(request):
    user_list = User_default.objects.all()
    user_dict = {'users_records':user_list}
    return render(request,'userInfo/user.html',context=user_dict)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Your are logged in!")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)# check the login info for you

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'userInfo/login.html', {})


def register_view(request):
    registered = False
    if request.method == "POST":

        login_form = forms.login_Form(data=request.POST)
        UserProfile_Form = forms.UserProfile_Form(data=request.POST)

        if login_form.is_valid() and UserProfile_Form.is_valid():
            user = login_form.save()
            user.set_password(user.password)
            user.save()

            profile = UserProfile_Form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(login_form.errors,UserProfile_Form.errors)

    else:
        login_form = forms.login_Form()
        UserProfile_Form = forms.UserProfile_Form()

    return render(request,'userInfo/registration.html',{'login_form':login_form,'UserProfile_Form':UserProfile_Form,'registered':registered})

def form_name_view(request):
    form = forms.model_Form()

    if request.method == "POST":
        form = forms.model_Form(request.POST)

        if form.is_valid():
            if form.save_user_form():
                print("VALIDATION SUCCESS and save into models!")
                print("First Name:",form.cleaned_data['first_name'])
                print("Last Name:",form.cleaned_data['last_name'])
                print("Email:",form.cleaned_data['email'])
                form.save(commit=True)
                return users(request)

            #print("TEXT:",form.cleaned_data['text'])


    return render(request,'userInfo/form_page.html',{'form':form})
