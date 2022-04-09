from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

import json as json
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, 'services.html')
def contact(request):
    print(request.body)
    
    if request.method == "POST":
      #  data = json.loads(request.body)

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, address=address, description=description,date=datetime.today())
        contact.save()
        print(name)
        messages.success(request, 'Your message has been saved successfully!')
    return render(request, 'contact.html')
