from django.shortcuts import render, redirect
from WebApp.forms import *
from WebApp.models import *
from django.shortcuts import render

def login_required_check(view):
    def updated_view(request):
        try:
            if request.session["loged_in"] == True:
                return view(request)
            else:
                return redirect(login)
        except KeyError:
            return redirect(login)

    return updated_view

def not_loged_in_check(view):
    def updated_view(request):
        try:
            if request.session["loged_in"] == False:
                return view(request)
            else:
                return redirect(index)
        except:
            return view(request)

    return updated_view


@login_required_check
def index(request):
    return render(request, "WebApp\\index.html")

@not_loged_in_check
def login(request):
    errorMessage = ''
    if request.method == 'POST':
        user_input = loginForms(request.POST)
        if user_input.is_valid():
            entered_username = user_input.cleaned_data["username"]
            entered_password = user_input.cleaned_data["password"]
            if Users.objects.filter(username=entered_username):
                if Users.objects.filter(username=entered_username).filter(password=entered_password):
                    request.session['username'] = entered_username
                    request.session['loged_in'] = True
                    return redirect(index)
                else:
                    request.session['loged_in'] = False
                    errorMessage = 'Wrong password'
            else:
                request.session['loged_in'] = False
                errorMessage = 'No such account'

    return render(request, "WebApp\\login.html", {
        'loginForm': loginForms(),
        'errorMessage': errorMessage
    })

@not_loged_in_check
def signup(request):
    if request.method == 'POST':
        user_input = signUpForms(request.POST)
        if user_input.is_valid():
            new_name = user_input.cleaned_data["name"]
            new_username = user_input.cleaned_data["username"]
            new_password = user_input.cleaned_data["password"]
            new_email = user_input.cleaned_data["email"]

            request.session['username'] = new_username
            request.session['loged_in'] = True

            new_user = Users(
                name=new_name,
                username=new_username,
                password=new_password,
                email=new_email
            )
            new_user.save()

            redirect(index)

    return render(request, "WebApp\\signup.html", {
        'signUpForm': signUpForms()
    })

@login_required_check
def logout(request):
    if request.method == 'POST':
        request.session['username'] = None
        request.session['loged_in'] = False
        return redirect(login)
    else:
        return render(request, "WebApp\\logout.html")