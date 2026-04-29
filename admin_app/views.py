from django.shortcuts import render,redirect
from tripza .models import user_details
from .models import *

# Create your views here.
def user_view(request):
    data=user_details.objects.all()
    return render(request,'user_view.html',{'result':data})




def addpackage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        location = request.POST.get('location')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        duration=request.POST.get('duration')

        data=add_package(
            name=name,
            description=description,
            price=price,
            location=location,
            category=category,
            image=image,
            duration=duration
        )
        data.save()

        return redirect("add_package")  # reload page

    return render(request, 'add_pac.html')

def package_update(request,id):
    package = add_package.objects.get(pk=id)
    return render(request,'package_update.html',{'result':package})



def update_package(request, id):
    
    package = add_package.objects.get(pk=id)
    if request.method == 'POST':
        package.name = request.POST.get('name')
        package.description = request.POST.get('description')
        package.price = request.POST.get('price')
        package.location = request.POST.get('location')
        package.category = request.POST.get('category')
        package.duration=request.POST.get('duration')

        if request.FILES.get('image'):
            package.image = request.FILES.get('image')

        package.save()
        return redirect('admin_package_view')

    return render(request, 'package_update.html', {'package': package})



def delete_package(request, id):
    package = add_package.objects.get(pk=id)
    package.delete()
    return redirect('admin_package_view')  

def admin_package_view(request):
    data=add_package.objects.all()
    return render(request,'adminpac_view.html',{'result':data})
