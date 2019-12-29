from django.shortcuts import render
from django.utils import timezone
from .models import ContactInfo
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    return render(request, 'ContactApp/index.html')


@login_required
def add_contact(request):

    added_name = request.POST.get("contactName")
    added_number = request.POST.get("contactNumber")
    added_email = request.POST.get("contactEmail")

    contacts = ContactInfo.objects.filter(user=request.user)

    for contact in contacts:
        if contact.name == added_name:
            messages.info(request, 'The Contact Name already exists! Try something different.')
            return HttpResponseRedirect("/loggedin/")

    ContactInfo.objects.create(user = request.user, name = added_name, number = added_number, email = added_email)

    return HttpResponseRedirect("/")
    

@login_required
def contacts_list(request):
    contacts = ContactInfo.objects.filter(user=request.user).order_by("-date")

    context_dict = {
        "contacts" : contacts,
    }

    return render(request, 'ContactApp/list.html', context_dict)


@login_required
def delete_contact(request, contact_id):

    ContactInfo.objects.filter(user=request.user).get(id=contact_id).delete()

    return HttpResponseRedirect("/contacts_list")


@login_required
def edit_contact(request, contact_id):
    edited_contact = ContactInfo.objects.filter(user=request.user).get(id=contact_id)
    context_dict = {
        "contactName" : edited_contact.name,
        "contactNumber" : edited_contact.number,
        "contactEmail" : edited_contact.email,
    }
    ContactInfo.objects.filter(user=request.user).get(id=contact_id).delete()
    return render(request, 'ContactApp/edit.html', context_dict)





