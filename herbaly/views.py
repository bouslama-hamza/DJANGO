from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm , UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from herbaly.pandas import request_data_base
from herbaly.pyplot import make_pie , make_plot
from herbaly.send_email import send_email
from django.contrib.auth.models import User

# this views for the home page
def home(request):
    return render(request , 'home.html' ,{'title' : 'Home'})

# this views for the sign_up page
def sign_up(request):
    if request.method == 'POST':
        make_email = request.POST["make_email"]
        send_email(make_email , make_email,'send')
        message = 'Your Email Has Been Sent successfully'
        return render(request , 'sign_up.html' , {'message':message , 'title' : 'Sign Up'})
    return render(request , 'sign_up.html' ,{'title' : 'Sign Up'})

# this views for the app page
@login_required
def app(request):
    if request.method == 'POST':
        make = request.POST["test"]
        base = 'herbaly/static/EXCEL/'+make
        data_base = request_data_base(base, 'Excel')
        make_plot(base,'Excel')
        make_pie(base ,'Excel')
        return render(request , 'data_base.html' , {'data_base' : data_base ,'title' : 'Data Base'})
    return render(request , 'app.html' , {'title' : 'App'})

# this views for the active account page
@login_required
def active_account(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance = request.user)
        if update_form.is_valid():
            request.user.set_password(update_form.cleaned_data.get('password2'))
            update_form.save()
            message = 'Setting has been adding Successfully'
            return render(request , 'active_account.html' , {'update_form':update_form , 'message':message , 'title' : 'Active Account'})
        else:
            error = 'Invalid Information Please Try Again'
            return render(request , 'active_account.html' , {'update_form':update_form , 'error':error , 'title' : 'Active Account'})
    else:
        update_form = UserUpdateForm(instance = request.user)
    return render(request , 'active_account.html' , {'update_form':update_form , 'title' : 'Active Account'})

# this views for the google cloud page
@login_required
def google_cloud(request):
    if request.method == 'POST':
        big_query = request.POST["big_query"]
        data_base = request_data_base(big_query,'Query')
        make_plot(big_query,'Query')
        make_pie(big_query ,'Query')
        return render(request, "data_base.html" , {'data_base' : data_base , 'title' : 'Data Base'})
    return render(request , 'google_cloud_data_base.html' , {'title' : 'Google Cloud'})

# this views for the manage account page
@login_required
@staff_member_required
def manage_account(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            send_email(form.cleaned_data.get('username') ,form.cleaned_data.get('password1') ,'request')
            message = f'Account Have been created succesfuly for {first_name} {last_name}'
            return render(request , 'manage_account.html' ,{'message':message , 'form':form , 'title' : 'Manage Account'})
        else:
            error = 'Invalid Information Please Try Again'
            return render(request , 'manage_account.html' ,{'error':error , 'form':form  , 'title' : 'Manage Account'})
    else:
        form = UserRegisterForm()
    return render(request , 'manage_account.html' , {'form':form , 'title' : 'Manage Account'})

# this views for the forget password page
def forget_password(request):
    global change_number
    global user
    if request.method == 'POST':
        email = request.POST['change_email']
        try :
            user = User.objects.get(email = email)
            change_number = send_email(user.email , user.email , 'change')
            return render(request ,'change_password.html' , {'title' : 'Change Password'})
        except:
            message = 'This User Dont Have An Account , please chaque your information'
            return render(request , 'forget_password.html' , {'message':message , 'title' : 'Forget Password'})
    return render(request , 'forget_password.html' , {'title' : 'Forget Password'})

# this views for the change password page
def change_password(request):
    if request.method == 'POST':
        if change_number != int(request.POST['change_password']):
            message = 'Error !,wrong Number please chaque and try Again'
            return render(request , 'change_password.html' , {'message' : message , 'title' : 'Change Password'})
        elif request.POST['password_change'] != request.POST['conf_password_change']:
            error = 'Error!, Password and Confirm password are not the same'
            return render(request , 'change_password.html' , {'error' : error , 'title' : 'Change Password'})
        else:
            user.set_password(request.POST['conf_password_change'])
            user.save()
            form = UserLoginForm()
            messages = 'Your password has been change Successfully'
            return render(request , 'sign_in.html' , {'form' : form , 'messages' : messages , 'title' : 'Sign In'})
    return render(request , 'change_password.html' , {'title' : 'Change Password'})

# this views for the data base page
@login_required
def data_base(request):
    return render(request , 'data_base.html' , {'title' : 'Data Base'})
