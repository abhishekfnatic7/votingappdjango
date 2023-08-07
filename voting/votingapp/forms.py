from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User


class Userform(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Password is required'})
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Confirm Password is required'})
    email=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}),error_messages={'required':'Email is required'})
    class Meta:
        model=User
        fields=['username','email']
        widgets = {
            "username": forms.TextInput(attrs={'class':'form-control'}),
                }
       
        error_messages = {    
            "username": {"required": ("Username is required")},
            }

        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password1")
        cpassword = cleaned_data.get("password2")
        email = cleaned_data.get("email")
        
        if password!=cpassword:
            raise forms.ValidationError("Password did not match")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already taken")
        
    
class Loginform(AuthenticationForm):
    username=forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control mb-2'}),error_messages={'required':'Username is required'})
    password=forms.CharField(max_length=150,required=True,widget=forms.PasswordInput(attrs={'class':'form-control mb-2'}),error_messages={'required':'Password is required'})

    class Meta:
        model=User
        fields=['username','password']
        

# class Votingform(forms.ModelForm):

#     class Meta:
#         model=Vote
#         fields="__all__"
#         widgets={

#             'option1':forms.RadioSelect(attrs={'class':'form-control'}),
#             'option2':forms.RadioSelect(attrs={'class':'form-control'}),
#             'option3':forms.RadioSelect(attrs={'class':'form-control'}),
#             'option4':forms.RadioSelect(attrs={'class':'form-control'})
            
#         }