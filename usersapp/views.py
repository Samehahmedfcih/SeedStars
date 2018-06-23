import sys
from django.shortcuts import render
from django.http import HttpResponse
from usersapp import models
from usersapp import  forms
from django.forms.utils import ErrorList

# Create your views here.

#Welcome Page
def Welcome(request):
   return  render(request,'welcome.html')



#Add new user page
def ADD(request):

  form_data=forms.UserRegister(request.POST or None)
  msg=''
  excep =''
  try:
    if request.method == 'POST':
        #check is data valid in post request
        if form_data.is_valid():
            User=models.User()
            User.Email=form_data.cleaned_data['Email']
            User.Name=form_data.cleaned_data['Name']
            User.save();
            msg = 'data saved sussecfully '
        #Post request bu has invalid data
        else :
            form_data =forms.UserRegister(request.POST,error_class=forms.DivErrorList)
            excep = 'Form  Validation Error'
    #if it's Get Request

  #handling any Exception that may occure
  except Exception as e:
      excep = e

  finally:
      context = {
          'UserRegisterForm': form_data,
          'msg': msg,
          'excep' : excep
      }
      return render(request, 'AddUser.html', context)



#list all users page

def listAllUsers(request ) :
    UsersList = models.User.objects.all()
    context={
        'Users':UsersList
    }
    return render(request, 'ListAllUsers.html', context)
