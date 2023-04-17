from django.shortcuts import render
from .models import *
# Create your views here.
def home (request):
    sherbimet = Sherbimet.objects.all()
    context ={"sherbimet":sherbimet}
    if request.method == "POST":
        name_contact = request.POST["name"]
        mosha_contact = request.POST["mosha"]
        tel_contact = request.POST["tel"]
        problema_contact = request.POST["problema"]

        Contact(contact_name=name_contact, contact_mosha=mosha_contact, 
        contact_tel = tel_contact, contact_problema=problema_contact).save()
    return render(request, 'home.html', context)

def about (request):
    return render(request, 'about.html')

def contact (request):
    if request.method == "POST":
        name_contact = request.POST["name"]
        mosha_contact = request.POST["mosha"]
        tel_contact = request.POST["tel"]
        problema_contact = request.POST["problema"]

        Contact(contact_name=name_contact, contact_mosha=mosha_contact, 
        contact_tel = tel_contact, contact_problema=problema_contact).save()
        # return render(request, 'contact.html')
    return render(request, 'contact.html')

def service (request):
    sherbimet = Sherbimet.objects.all()
    context ={"sherbimet":sherbimet}
    return render(request, 'service.html', context)

