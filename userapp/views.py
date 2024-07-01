from django.shortcuts import render,redirect,get_object_or_404
from django.utils.crypto import get_random_string
from django.contrib import messages
from userapp.models import *
from complaint.blackchain import  BlockChain
from django.db import connection
import os
# import requests
# import hashlib


# Create your views here.
def user_login(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = UserModel.objects.get(user_email=email, user_password=password)
            request.session['user_id'] = user.user_id
            messages.info(request, "Login Successfully.")
            return redirect("user_index")        
        except:
            print('error')
            messages.error(request,"Invalid EmailID or Password")         
    return render(request, 'main/home-userlogin.html')

def user_register(request):
    if request.method == "POST" and request.FILES['userphoto']:
        user_name=request.POST['username']
        user_email=request.POST['email']
        user_password=request.POST['password']
        user_phone=request.POST['phonenumber']
        user_city=request.POST['city']
        user_pic=request.FILES['userphoto']
        
        try:
            UserModel.objects.get(user_email=user_email)
            messages.error(request, "User Email Already Exit.")
            return redirect('user_rigister')
        except:
                               
            UserModel.objects.create(user_name=user_name, user_email=user_email, user_password=user_password,
                                             user_phone=user_phone, user_city=user_city, user_pic=user_pic)
            messages.info(request, "Registration Successfully.")
            return redirect('user_login')
    else: 
        return render(request, 'main/home-user-register.html')  

def user_index(request):
    a = UserModel.objects.all().count()
    b = ComplaintModel.objects.all().count()
    c = FeedbackModel.objects.all().count()
    d = ComplaintModel.objects.filter(status='Pending').count()
    return render(request,'user/user-index.html',{'a':a,'b':b,'c':c,'d':d})  

def user_profile(request):
    user_id = request.session['user_id']
    j = UserModel.objects.get(user_id=user_id)
    obj = get_object_or_404(UserModel, user_id=user_id)
    if request.method == 'POST':
        user_name=request.POST['username1']
        user_email=request.POST['email']
        user_password=request.POST['password']
        user_phone=request.POST['phonenumber']
        user_city=request.POST['city']
        print(user_phone)
        # user_pic=request.FILES['userphoto']
       
        if not request.FILES.get("userphoto",False):
            # print("yes efffeg jfkdftjhkt")
            obj.user_name = user_name
            obj.user_email = user_email
            obj.user_password = user_password
            obj.user_phone = user_phone
            obj.user_city = user_city
            
            obj.save(update_fields=['user_name', 'user_email', 'user_phone',
                                        'user_city', 'user_password'])
            obj.save()
             
        elif request.FILES.get("userphoto",False):
            user_pic = request.FILES['userphoto']
            obj.user_name = user_name
            obj.user_email = user_email
            obj.user_phone = user_phone
            obj.user_city = user_city
            obj.user_password = user_password
            obj.user_pic = user_pic
            obj.save(update_fields=['user_name', 'user_email', 'user_phone',
                                        'user_city', 'user_password', 'user_pic'])
            obj.save()
           
           
        messages.info(request, 'Profile Updated Successfully.')
        return redirect('user_profile')
    else:
        return render(request,'user/user-myprofile.html',{'j':j})

def add_complaint(request):
    user_id = request.session['user_id']
    # j = UserModel.objects.get(user_id=user_id)
    j = get_object_or_404(UserModel, user_id=user_id)
    
    if request.method == "POST" and request.FILES['evidence']:
        suspect_name=request.POST['suspectname']
        Complaint_type=request.POST['complainttype']
        Evidence =request.FILES['evidence']
        Approx_date=request.POST['aproxdate']
        occured_place=request.POST['place']
          
    
        h = ComplaintModel.objects.create(suspect_name=suspect_name, Complaint_type=Complaint_type,Evidence=Evidence, Approx_date=Approx_date,
                                             occured_place=occured_place,user=j)
        # h = ComplaintModel.objects.get(suspect_name=suspect_name, Complaint_type=Complaint_type, Approx_date=Approx_date,
        #                                      occured_place=occured_place,user=j)
        
        
        key = 'qazwsxedcrfvtgbyhn'
        
        #First Block
        suspect = h.suspect_name
        inital_block = BlockChain(key,[suspect])
        a =inital_block.block_hash
        print(a)
        h.suspect_block_chain = a
        h.save(update_fields=['suspect_block_chain'])
        h.save()
        
        #Second Block 
        complaint = h.Complaint_type
        second_block = BlockChain(key,[complaint])
        b =second_block.block_hash
        print(b)
        h.Complaint_type_block_chain = b
        h.save(update_fields=['Complaint_type_block_chain'])
        h.save()
        
        
        #Third Block
        date = str(h.Approx_date)
        third_block = BlockChain(key,[date])
        c =third_block.block_hash
        print(c)
        h.Approx_date_block_chain = c
        h.save(update_fields=['Approx_date_block_chain'])
        h.save()
        
        #Fourth Bloack
        occured = h.occured_place
        fourth_block = BlockChain(key,[occured])
        d =fourth_block.block_hash
        print(d)
        h.occured_place_block_chain = d
        h.save(update_fields=['occured_place_block_chain'])
        h.save()
        
        #Fivth Block
        enc=open(os.path.abspath('media/' + str(h.Evidence)).replace("\\","/"), 'rb')
        img=enc.read()
        enc.close()
        evidence = str(img)
        fivth_block = BlockChain(key,[evidence])
        e =fivth_block.block_hash
        print(e,'file this is')
        h.Evidence_block_chain = e
        h.save(update_fields=['Evidence_block_chain'])
        h.save()
        
        
        messages.info(request, "Complaint Sent Successfully.")       
        return redirect('user_index')
    else: 
        return render(request,'user/user-add-complaints.html')    
      
def check_complaint(request):
    user = request.session['user_id']
    check = ComplaintModel.objects.filter(user=user)
    return render(request,'user/user-complaint-status.html',{'check':check})

def all_complaints(request):
    user = request.session['user_id']
    check = ComplaintModel.objects.filter(user=user)
    return render(request,'user/user-all-complaints.html',{'check':check})

def user_feedback(request):
    user = request.session['user_id']
    user_id = UserModel.objects.get(user_id=user)
    if request.method == "POST":
        if not request.POST.get('a'):
            messages.error(request, "Feeback not Sent Please give the star Rating")
            return redirect('user_feedback')
        star = request.POST.get('a')
        comment = request.POST.get('comment')        
        FeedbackModel.objects.create(star=star,comment=comment,user=user_id)
        messages.info(request, "Feedback Sent Successfully.")
        return redirect('user_index') 
    else:
        return render(request,'user/user-feedback.html')

