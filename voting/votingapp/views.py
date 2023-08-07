from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Userform,Loginform
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Vote,Voteuser
from django.contrib.auth.models import User
# Create your views here.
def studentsignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=Userform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your account is created successfully')
                return redirect('studentsignup')

        else:
            fm=Userform()
        return render(request,'studentsignup.html',{'u':fm})
    else:
        return redirect('home')

def studentlogin(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            a=Loginform(request=request,data=request.POST)
            if a.is_valid():
                username=a.cleaned_data['username']
                password=a.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
        else:
            a=Loginform(request)
        return render(request,'studentlogin.html',{'u':a})
    else:
        return redirect('home')
    
@login_required()
def studentlogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='studentlogin')
def home(request):
    a=Vote.objects.prefetch_related('user')
    b=Vote.objects.filter(user=3).last()
   
    c=Voteuser.objects.filter(user=request.user.id)
    
    return render(request,'home.html',{'a':a,'c':c})

def vid(request):
    if request.method =='GET':
        dataid=request.GET['a']
        checkval=request.GET['b']
        
        c=Vote.objects.get(id=dataid)
        d=c.user.filter(username=request.user.username).first()
        vc=Voteuser.objects.filter(user__username=request.user.username).values('qid','user','ochosen').last()

        if str(d)==request.user.username:
            # c.user.remove(request.user.id)
            c.vote=c.vote
            if vc['qid']==c.id and vc['user']==request.user.id:
               
                
                if vc['ochosen']==c.option1:
                   
                
                    c.option1val=c.option1val-1

                    if c.option2==checkval:
                        c.option2val+=1
                    elif c.option3==checkval:
                        c.option3val+=1
                    elif c.option4==checkval:
                        c.option4val+=1

                    else:
                        c.vote=c.vote-1
                        c.user.remove(request.user.id)


                   
                    
                elif vc['ochosen']==c.option2:
                    
                    c.option2val=c.option2val-1
                    
                    if c.option1==checkval:
                        c.option1val+=1
                    elif c.option3==checkval:
                        c.option3val+=1
                    elif c.option4==checkval:
                        c.option4val+=1

                    else:
                        c.vote=c.vote-1
                        c.user.remove(request.user.id)


                    
                    
                elif vc['ochosen']==c.option3:
                    c.option3val=c.option3val-1
                    
                    if c.option1==checkval:
                        c.option1val+=1
                    elif c.option2==checkval:
                        c.option2val+=1
                    elif c.option4==checkval:
                        c.option4val+=1

                    else:
                        c.vote=c.vote-1
                        c.user.remove(request.user.id)

                   
                elif vc['ochosen']==c.option4:
                    c.option4val=c.option4val-1
                    
                    if c.option1==checkval:
                        c.option1val+=1
                    elif c.option2==checkval:
                        c.option2val+=1
                    elif c.option3==checkval:
                        c.option3val+=1

                    else:
                        c.vote=c.vote-1
                        c.user.remove(request.user.id)

                    
            
            c.save()
            e=Voteuser.objects.create(ochosen=checkval,qid=dataid)
            e.user.add(request.user.id)
            e.save()
            
        
        else:    
            c.user.add(request.user.id)
            c.vote+=1
            if c.option1==checkval:
                c.option1val+=1
            elif c.option2==checkval:
                c.option2val+=1
            elif c.option3==checkval:
                c.option3val+=1
            elif c.option4==checkval:
                c.option4val+=1
           
            c.save()
            e=Voteuser.objects.create(ochosen=checkval,qid=dataid)
            e.user.add(request.user.id)
            e.save()
            

        return JsonResponse({"data":"s"},safe=False)




