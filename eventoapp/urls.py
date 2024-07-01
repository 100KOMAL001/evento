from django.urls import path
from eventoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('index',views.index1),
     path('register',views.register),
     path('login',views.Ulogin),
     path('logout',views.user_logout),
     path('contact', views.contact1, name='contact'),
     path('service', views.service),
     path('price', views.price),
     path('about',views.about),
     path('gallery',views.gallery),
     path('views_details/<Pid>',views.views_detail),
     path('book/<pid>',views.book),
     path('pay/<pid>',views.pay),
     path('paymentsuccess',views.paymentsuccess),
     path('booking-history', views.booking_history, name='booking-history'), 

    # path('payment',views.payment),
    #path('addtocart',views.addtocart), 
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)