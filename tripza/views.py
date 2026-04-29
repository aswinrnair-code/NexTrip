from django.shortcuts import render,redirect
from .models import user_details,bookingtemp
from admin_app .models import add_package
from django.conf import settings
import razorpay
from .models import payment



# Create your views here.
def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def trips(request):
    return render(request,'trips.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        if user_details.objects.filter(email=email).exists():
            return render(request,'register.html',{
                'error':'user already exists'
            })
        
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        data=user_details(name=name,email=email,phone=phone,password=password)
        data.save()
    return render(request,'registration.html') 

def login(request):
    email= request.POST.get('email')
    password = request.POST.get('password')

    if email =='admin123@gmail.com' and password =='2233':
        request.session['email'] = email
        request.session['password']=password
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login success'})

    elif user_details.objects.filter(email=email,password=password).exists():
        user=user_details.objects.get(email=request.POST['email'],password=password)
        if user.password == request.POST['password']:
            request.session['uid'] = user.id
            request.session['uname'] = user.name
            request.session['uphone'] = user.phone
            request.session['user'] = 'user'
            return render(request,'index.html', {'status': 'user login success'})
        

    else:
        return render(request, 'login.html', {'status': 'login failed'})
    

def costarica(request):
    return render(request,'costarica.html')

def logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect(index)


def tempbooking(request):
    
    # ✅ Always fetch packages for dropdown
    packages = add_package.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        package_id = request.POST.get('package')
        travel_date = request.POST.get('travel_date')
        travelers = request.POST.get('travelers')
        pickup = request.POST.get('pickup')
        spec_req = request.POST.get('spec_req')
        user_id = request.user.id

        # ✅ Get full package object from DB
        package_obj = add_package.objects.get(id=package_id)

        # ✅ Save booking with real data
        data = bookingtemp(
            name=name,
            email=email,
            phone=phone,
            package=package_obj.name,
            price=package_obj.price,
            travel_date=travel_date,
            travelers=travelers,
            pickup=pickup,
            spec_req=spec_req,
            user_id=user_id
        )
        data.save()

        client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, 
        settings.RAZORPAY_KEY_SECRET)
        )
        amount = int(package_obj.price) * 100  # paise
        payment_order = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1
        })

        return render(request, 'payment.html', {
            'order_id': payment_order['id'],
            'amount': amount,
            'key': settings.RAZORPAY_KEY_ID,
            'name': name,
            'email': email,
            'phone': phone,
            'booking_id': data.id,
        })

    # return render(request, 'booking.html', {'packages': packages})

        # return redirect('index')  # better than render after POST

    # ✅ Send packages to template for dropdown
    return render(request, 'booking.html', {'packages': packages})

def payment_success(request):
    payment_id = request.GET.get('payment_id')
    booking_id = request.GET.get('booking_id')
    # optionally save payment_id to booking record
    return render(request, 'payment_success.html', {
        'payment_id': payment_id
    })

def book_update(request,id):
    data=add_package.objects.get(pk=id)
    return render(request,'index.html',{'result':data})

def my_bookings(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    bookings = bookingtemp.objects.filter(
        user_id=request.user.id
    ).order_by('-id')
    
    return render(request, 'my_bookings.html', 
                  {'bookings': bookings})


     
