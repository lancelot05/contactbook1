from django.shortcuts import render
from django.utils import timezone
from .models import ContactInfo
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request, 'ContactApp/index.html')


def add_contact(request):

    added_name = request.POST.get("contactName")
    added_number = request.POST.get("contactNumber")
    added_email = request.POST.get("contactEmail")

    contacts = ContactInfo.objects.all()

    for contact in contacts:
        if contact.name == added_name:
            messages.info(request, 'The Contact Name already exists! Try something different.')
            return HttpResponseRedirect("/")

    created_contact = ContactInfo.objects.create(name = added_name, number = added_number, email = added_email)

    return HttpResponseRedirect("/")
    


def contacts_list(request):

    contacts = ContactInfo.objects.all().order_by("-date")

    context_dict = {
        "contacts" : contacts,
    }

    return render(request, 'ContactApp/list.html', context_dict)

def delete_contact(request, contact_id):

    ContactInfo.objects.get(id=contact_id).delete()

    return HttpResponseRedirect("/contacts_list")
