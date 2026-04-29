from django.shortcuts import render,redirect
from tripza .models import user_details
from admin_app .views import user_view
# Create your views here.
def userprofile(request):
    uid=request.session['uid']
    pro_data=user_details.objects.get(pk=uid)
    return render(request,'user_profile.html',{'result':pro_data})
def user_delete(request,id):
    data=user_details.objects.get(pk=id)
    data.delete()
    return redirect(user_view)
def user_update(request,id):
    data=user_details.objects.get(pk=id)
    return render(request,'user_update.html',{'result':data})
def user_updates(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        data=user_details(id=id,name=name,email=email,phone=phone,password=password)
        data.save()
        return redirect(user_view)
    return render(request,'user_update.html')

