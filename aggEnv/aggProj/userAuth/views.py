from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib import messages
import time
# import requests
from .models import *
from .forms import *

#####################################################################################

# https://stackoverflow.com/questions/55034707/django-redirecting-to-a-different-view-in-another-app
# https://docs.djangoproject.com/en/1.10/topics/auth/
# https://docs.djangoproject.com/en/1.10/topics/auth/default/
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

#####################################################################################

def userRegistration(request):
    # user_reg = Users.objects.all().values()  
    template = loader.get_template('userRegistration.html')
      
    
    if request.method == 'POST':
        form = user_data(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']
            form.save()
            messages.success(request, "Registration Successful.")
            return redirect("userAuth:userLogin")
            # ("app_name_url_name") ^
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        # this must be a GET request, so create an empty form
        form = user_data()
    
    form = user_data()     
    context = {
        # 'user_reg': user_reg, 
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
##########################################################################################

def userLogin(request):
    template = loader.get_template('userLogin.html')
    message = ""
    
    
    if request.method == "POST":
        
        form = Users(request.POST or None, request.FILES or None)        
        ip_email = request.POST.get('email')
        ip_password = request.POST.get('password')
        print("email", ip_email)
        print("pw", ip_password)
        
        
        try:
            q_pw = Users.objects.values("password").get(email = ip_email)
            print("pw from query", q_pw["password"])
            if Users.objects.get(email = ip_email):
                print("here 1")
                if ip_password == q_pw["password"]:
                    
                    message = "login successful"
                    time.sleep(3)
                    return redirect("aggApp:paginate_page")
                            # ("app_name_url_name") ^
                            
                else: 
                    print("here 2")
                    message = "password incorrect"
                    
            else:
                print("here 3")
                try:
                    user = Users.objects.get(email=ip_email)
                except Users.DoesNotExist:
                    message = "email incorrect"
        except Users.DoesNotExist:
            print("here 44")
            message = "User doesnot exist"
    else:
        # this must be a GET request, so create an empty form
        form = user_data()
    
    form = user_data() 
    
    context = {
        # 'user_reg': user_reg, 
        'form' : form,
        'message' : message,
        
        # 'ip_email' : ip_email,
        # 'ip_password' : ip_password,
    }    
    return HttpResponse(template.render(context, request))


# def userLogin(request):
#      template = loader.get_template('userLogin.html')
     
#      context ={
         
#      }
#      return HttpResponse(template.render(context, request))
    
#########################################################################################

def logout_request(request):
	# logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("userLogin")
