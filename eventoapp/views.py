from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Contact 
from .models import  Package,Event
import simplejson as json
import razorpay 
from django.core.mail import send_mail
from .models import BookingHistory



#from eventoapp.mods import Product

# Create your views here.
def index1(request):
    return render(request,'index.html')
def register(request):
    context={}
    
    if request.method=='GET':
        return render(request,'register.html')
    else:
        un=request.POST['uname']
        ue=request.POST['uemail']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        
        if un=='' or p=='' or cp=='':
            context['errmsg']='field can not br blank..!'
            return render(request,'register.html',context)
        elif p!=cp:
            context['errmsg']="password & confirm password must be same..! "
            return render(request,'register.html',context)
        elif len(p)<8:
            context['errmsg']='password should be greater then 8 characters..'
            return render(request,'register.html',context)
        else:
            u=User.objects.create(username=un,email=ue)
            u.set_password(p)
            u.save()
            context['success']='Data Inserted successfully..||'
            return render(request,'register.html',context)
def Ulogin(request):
    context={}
    if request.method=='GET':
        return render(request,'login.html')
    else:
        n=request.POST['uname']
        p=request.POST['upass']
       # print(n," ",p)
        u=authenticate(username=n,password=p)
        print(u)
        if u is not None:
            login(request,u)
            return redirect('/index')
        else:
            context['errmsg']='Invalid Username & Password'
            return render(request,'login.html',context)
def user_logout(request):
    logout(request)
    return redirect('/login')
def contact1(request):
    context={}
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        context['success']='Data Inserted successfully..||'
     
     
    return render(request,'contact.html',context)
def service(request):
    return render(request,'service.html')
def price(request):
    packages = Package.objects.all()
    return render(request, 'price.html', {'data': packages})
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')

def views_detail(request,Pid):
    context={}
    p=Package.objects.filter(id=Pid)
    c=User.objects.filter(id=request.user.id)
    context['info']=c
    context['data']=p
    context['image']=p

   
    return render(request,'view_detail.html',context)

def book(request,pid):
    '''name = request.POST['name']
    venue = request.POST['venue']
    date = request.POST['date']
    time = request.POST['time']
    print(name,venue,date,time)
    if name and venue and date and time:
        event = Event.objects.create(name=name, venue=venue, date=date, time=time)
        event.save()'''
    
    p=Package.objects.filter(id=pid)
    context={}
    context['data']=p

    return render(request,'booking_detils.html',context)



 # Adjust the import based on your project structure





def pay(request,pid):
    name = request.POST['name']
    venue = request.POST['venue']
    date = request.POST['date']
    time = request.POST['time']
    i=Package.objects.filter(id=pid)[0]
    #print(name,venue,date,time,id)
    
    if name and venue and date and time:
        event = Event.objects.create(name=name, venue=venue, date=date, time=time,pid=i)
        event.save()

    u=User.objects.filter(id=request.user.id)
    #e=Event.objects.filter(pid=i)[0]


    h=BookingHistory.objects.create(uid=u[0],pid=i)
    h.save()


        # Initialize Razorpay client
    client = razorpay.Client(auth=("rzp_test_F7Os5lG3kREk3W", "a6UjTrG46l4Kt0Z4JFWzTG65"))

        # Get the package
    package = get_object_or_404(Package, id=pid)

        # Calculate the total amount (assuming you want the price of a single package)
    s = package.price
   # Create an order in Razorpay
    data = { "amount": s * 100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
   # Pass the payment information to the template
    context = {'payment': payment}
        
        #return HttpResponse(f"Error: {str(404)}", status=500)
    '''except razorpay.errors.RazorpayError as e:
        # Handle the error and show appropriate message
        return HttpResponse(f"Error: {str(e)}", status=500)'''

        
        
 
    return render(request, 'pay.html', context)


def paymentsuccess(request):
        
    


    # If the request method is not POST or conditions are not met, return a default response
    u=User.objects.filter(id=request.user.id)
    to=u[0].email
    sub='thanks for booking event'
    msg='thanku ..!!'
    frm='truptidevare0@gmail.com'
    send_mail(  # type: ignore
        sub,
        msg,
        frm,
        [to],
        fail_silently=False
    )


    return render(request, 'paymentsuccess.html')
   
   

'''u=User.objects.filter(id=request.user.id)
    to=u[0].email
    sub='E-commee Order status'
    msg='thanks for shopping...!!'
    frm='truptidevare0@gmail.com'
    send_mail(  # type: ignore
        sub,
        msg,
        frm,
        [to],
        fail_silently=False
    )

    return render(request, 'paymentsuccess.html', )    ''' 
def booking_history(request):
    
    h = BookingHistory.objects.filter(uid=request.user.id)
    context={}
    context['history']=h
    
    return render(request, 'booking_history.html',context)


    
    
    














