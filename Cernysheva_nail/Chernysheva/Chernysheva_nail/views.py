from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import View
from django.http import *

from .models import *
from .forms import *
# Create your views here.


def main_page(request):
    form = AppointmentForm(request.POST)
    return render(request, 'Chernysheva_nail/index.html', context={'form':form})


def post(request):
    if request.method == "POST":
        print('\nAppointmentForm(request.POST) == True\n')
        print(request.POST)
        form = AppointmentForm(request.POST)
        name_of_client=request.POST.get('name_of_client')
        second_name_of_client=request.POST.get('second_name_of_client')
        phone_number_of_client=request.POST.get('phone_number_of_client')
        chooise_appointment_service=request.POST.get('chooise_appointment_service')
        date_and_time_appointment=request.POST.get('date_and_time_appointment')

        if form.is_valid():
            print('\nappointment.save() == True\n')
            appointment = form.save()
            appointment.save()
            return HttpResponseNotModified()
        else:
            print('\n', form.errors.as_data())
            print('\nform.is_valid == False\n')
            return render(request, 'Chernysheva_nail/index.html', context={'form':form})
    elif request.method == "GET":
        return HttpResponse('')
    else:
        print('\nrequest.method != "POST"\n')
        print(request.POST)
        return render(request, 'Chernysheva_nail/index.html', context={'form':form})
