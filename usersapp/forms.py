from django import forms
from django.forms.utils import ErrorList

class DivErrorList(ErrorList):

     def __str__(self):
                 return self.as_divs()


     def as_divs(self):
          if not self: return ''

          return '<div class="errorlist">%s</div>' % ''.join([' <div class="alert alert-danger"><strong>%s</strong> </div>' % e for e in self])



class UserRegister(forms.Form ):
     Email= forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
     Name = forms.CharField(max_length=25,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))

