from django import forms
from django.utils import timezone
from logistapp.models import Trip
from django.contrib.auth.models import User

Location= [
    ('delhi', 'Delhi'),
    ('bangalore', 'Bangalore'),
    ('chennai', 'Chennai'),
    ]
Truck=[
('Flatbed Truck', 'flatbed Truck'),
('Garbage Truck', 'garbage Truck'),
('Dump Truck', 'dump Truck'),
]
class TripForm(forms.ModelForm):
    class Meta:
        model=Trip
        fields='__all__'

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')
    # widgets = {
    #     'source': forms.TextInput(attrs={'class': 'form-control',
    #                                                         }),
    #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
    # }
    #




    # source= forms.CharField(label='From', widget=forms.Select(choices=Location))
    # destination = forms.CharField(label='To', widget=forms.Select(choices=Location))
    # truck_type= forms.CharField(label='Truck Type', widget=forms.Select(choices=Truck))
    # Date_time = forms.DateTimeField()
