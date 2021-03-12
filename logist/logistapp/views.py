from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from logistapp.models import Trip
from logistapp.forms import TripForm,UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(TemplateView):
    template_name='index.html'

class TripListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'logistapp/trip_list.html'
    template_name='trip_list.html'
    model = Trip

class TripDetailView(DetailView):
    model=Trip
    template_name='trip_detail.html'

class CreateTripView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'logistapp/trip_detail.html'
    form_class=TripForm
    model=Trip

class TripUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'logistapp/trip_detail.html'
    form_class=TripForm
    model = Trip


class TripDeleteView(LoginRequiredMixin,DeleteView):
    model = Trip
    success_url = reverse_lazy('trip_list')

def register(request):

    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()
    return render(request,'registration/registration.html',{'user_form':user_form,'registered':registered})

# def Trip_Form(request):
#     form=forms.TripForm()
#     return render(request,'trip_form.html',{'form':form})
