from django.urls import path
from . import views

urlpatterns = [
    path('contacts_list/edit_contact/<int:contact_id>',
            views.edit_contact, name="EditContact"),
    path('delete_contact/<int:contact_id>',
            views.delete_contact, name="DeleteContact"),
    path('contacts_list/', views.contacts_list, name="ContactsList"),
    path('add_contact/', views.add_contact, name="AddContact"),
    path('', views.home, name="Home"),
    ]
