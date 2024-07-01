from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import ComplaintModel, UserModel, FeedbackModel
from django.contrib import messages
from complaint.blackchain import BlockChain
import os
from django.core.paginator import Paginator

# Create your views here.


def police_login(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get("name")
        password = request.POST.get("password")
        if name == "admin" and password == "admin":
            messages.info(request, "Login Successfully.")
            return redirect("police_dashboard")

        else:
            messages.error(request, "Invalid EmailID or Password")
            return redirect("police_login")
    return render(request, 'main/home-police.html')


def police_dashboard(request):
    a = ComplaintModel.objects.filter(status='Received').count()
    b = FeedbackModel.objects.all().count()
    c = UserModel.objects.all().count()
    return render(request, 'police/police-dashboard.html', {'a': a, 'b': b, 'c': c})


def view_complient(request):
    a = ComplaintModel.objects.filter(status='Received')
    p = Paginator(a, 10)
    page_number = request.GET.get('page')
    ServiceDatafinal = p.get_page(page_number)
    return render(request, 'police/police-view-complients.html', {'a': ServiceDatafinal})


def update_complient(request):
    a = ComplaintModel.objects.filter(status='In Process')
    p = Paginator(a, 10)
    page_number = request.GET.get('page')
    ServiceDatafinal = p.get_page(page_number)
    return render(request, 'police/police-update-complients.html', {'a': ServiceDatafinal})


def Complete(request, id):
    a = get_object_or_404(ComplaintModel, complaint_id=id)
    a.status = "Completed"
    a.save(update_fields=['status'])
    a.save()
    messages.info(request, "Case Completed Successfully")
    return redirect('police_dashboard')


def register(request, id):
    obj = ComplaintModel.objects.get(complaint_id=id)
    a = obj.suspect_name
    b = obj.Complaint_type
    c = obj.Approx_date
    date = str(c)
    d = obj.occured_place

    print(a, b, c)
    aa = obj.suspect_block_chain
    bb = obj.Complaint_type_block_chain
    cc = obj.Approx_date_block_chain
    dd = obj.occured_place_block_chain

    print(aa, bb, cc, dd)
    key = 'qazwsxedcrfvtgbyhn'
    inital_block = BlockChain(key, [a])
    e = inital_block.block_hash
    print(e, 'verifying')

    second_block = BlockChain(key, [b])
    f = second_block.block_hash
    print(f, 'verifying')

    third_block = BlockChain(key, [date])
    g = third_block.block_hash
    print(g, 'verifying')

    fourth_block = BlockChain(key, [d])
    i = fourth_block.block_hash
    print(i, 'verifying')
    try:
        enc = open(os.path.abspath(
            'media/' + str(obj.Evidence)).replace("\\", "/"), 'rb')
        img = enc.read()
        print(img, 'image dataaa')
        print(type(img), 'typeeee')
        print(len(img), 'length')
        string_data = str(img)
        print(type(string_data), 'stringsss')
        print(len(string_data), 'length string')
        fivfth_block = BlockChain(key, [string_data])
        print(fivfth_block.block_hash, 'hash')
        ia = fivfth_block.block_hash

        if e == obj.suspect_block_chain \
                and f == obj.Complaint_type_block_chain \
                and g == obj.Approx_date_block_chain \
                and i == obj.occured_place_block_chain \
                and ia == obj.Evidence_block_chain:
            messages.info(request, "Verified and Ready To Take Action")
            return render(request, 'police/police-registercase.html', {'i': obj})
        else:
            messages.error(request, "This Complaint has been Tampered")
    except:
        messages.error(request, "This Complaint has been Tampered")

    return redirect('police_dashboard')


def discard(request, id):
    a = get_object_or_404(ComplaintModel, complaint_id=id)
    if request.method == "POST":
        comment = request.POST.get('comment')
        a.Discard_reason = comment
        a.status = "Rejected"
        a.save(update_fields=['Discard_reason', 'status'])
        a.save()
        messages.info(request, "Discard Successfully")
        return redirect('police_dashboard')
    else:
        return render(request, 'police/police-discard-case.html')


def view_feedback(request):
    a = FeedbackModel.objects.all()
    p = Paginator(a, 5)
    page_number = request.GET.get('page')
    ServiceDatafinal = p.get_page(page_number)
    return render(request, 'police/police-view-feedbacks.html', {'a': ServiceDatafinal})


def fill_FIR(request, id):
    a = get_object_or_404(ComplaintModel, complaint_id=id)
    a.Case_fill_as = "FIR"
    a.status = 'In Process'
    a.save(update_fields=['Case_fill_as', 'status'])
    a.save()
    messages.info(request, "Case fill as FIR")
    return redirect('police_dashboard')


def fill_NCR(request, id):
    a = get_object_or_404(ComplaintModel, complaint_id=id)
    a.Case_fill_as = "NCR"
    a.status = 'In Process'
    a.save(update_fields=['Case_fill_as', 'status'])
    a.save()
    messages.info(request, "Case fill as NCR")
    return redirect('police_dashboard')


def all_complaints(request):
    a = ComplaintModel.objects.filter(status='Completed')
    p = Paginator(a, 10)
    page_number = request.GET.get('page')
    ServiceDatafinal = p.get_page(page_number)
    return render(request, 'police/police-all-complaints.html', {'a': ServiceDatafinal})
