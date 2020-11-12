from django.shortcuts import render
from .models import Items,Contact
from math import ceil

# Create your views here.

def home(request):
   items=Items.objects.all()
   print(items)
   n=len(items)
   nSlides=n//4+ceil((n/4)-(n//4))
   params={'no_of_slides':nSlides,'range':range(1,nSlides),'items':items}
   return render(request,'manufacture/home.html',params)

def about(request):
   return render(request,'manufacture/about.html')

def contact(request):
   if request.method=='POST':
      first_name=request.POST.get('first_name','')
      last_name=request.POST.get('last_name','')
      email=request.POST.get('email','')
      company=request.POST.get('company','')
      website=request.POST.get('website','')
      phone=request.POST.get('phone','')
      address=request.POST.get('address','')
      your_enquiry=request.POST.get('your_enquiry','')
      industry=request.POST.get('industry','')
      product_type=request.POST.get('product_type','')
      contact=Contact(first_name=first_name,last_name=last_name,email=email,company=company,website=website,phone=phone,address=address,your_enquiry=your_enquiry,industry=industry,product_type=product_type)
      contact.save()   
   return render(request,'manufacture/contact.html')