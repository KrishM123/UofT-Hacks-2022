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
    if request.session["type"] == 'Student':
        return render(request, "WebApp\\studentindex.html", {"name": str(Users.objects.filter(username=request.session["username"])).split(": ")[1]})
    else:
        return render(request, "WebApp\\teacherindex.html", {"name": str(Users.objects.filter(username=request.session["username"])).split(": ")[1]})

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
                    request.session['type'] = Users.objects.filter(username=entered_username).filter(password=entered_password).type
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
            new_type = user_input.cleaned_data["type"]
            new_email = user_input.cleaned_data["email"]

            request.session['username'] = new_username
            request.session['loged_in'] = True
            request.session['type'] = new_type

            new_user = Users(
                name=new_name,
                username=new_username,
                password=new_password,
                type=new_type,
                email=new_email
            )
            new_user.save()
            return redirect(index)

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

@login_required_check
def post(request):
    if request.session["type"] == 'Teacher':
        if request.method == 'POST':
            user_input = signUpForms(request.POST)
            if user_input.is_valid():
                new_question = user_input.cleaned_data["question"]
                option1 = user_input.cleaned_data["Option1"]
                option2 = user_input.cleaned_data["Option2"]
                option3 = user_input.cleaned_data["Option3"]
                option4 = user_input.cleaned_data["Option4"]
                new_answer = [user_input.cleaned_data["Option"+str(n)] for n in range(1, 5)][int(user_input.cleaned_data["answer"]) - 1]
                tags = ', '.join([user_input.cleaned_data["Tag"+str(n)] for n in range(1, 11)])

                question = Question(
                    question=new_question,
                    option1=option1,
                    option2=option2,
                    option3=option3,
                    option4=option4,
                    answer=new_answer,
                    tage=tags
                )
                question.save()

        return render(request, "WebApp\\post.html", {
            'createQuestion': createQuestion()
        })
    return redirect(index)

