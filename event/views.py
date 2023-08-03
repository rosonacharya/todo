from django.shortcuts import render, HttpResponse
from event import models
# Create your views here.
def index(request):
    context={'success': False}
    if request.method =="POST":
        user=request.POST['user']
        email=request.POST['email']
        phone=request.POST['phone']
        list=request.POST['list']
        #print(user,email,phone,list)
        task=models.task(user=user,email=email,phone=phone,list=list)
        task.save()
        context={'success':True}
    return render(request,"index.html",context)
def event(request):
    allevent=models.task.objects.all()
    context={'task':allevent}

    
    return render(request,"event.html",context)    
        
         