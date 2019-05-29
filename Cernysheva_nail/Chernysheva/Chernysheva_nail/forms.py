from django import forms
from .models import *
from django.forms import ModelForm, TextInput, SelectMultiple, Select




class AppointmentForm(forms.ModelForm):
    class Meta:

        model = Appointment

        fields = (
         'name_of_client',
         'second_name_of_client',
         'phone_number_of_client',
         'chooise_appointment_service',
         'date_and_time_appointment',
         )
        widgets = {
            'name_of_client': TextInput(attrs={
             'class': 'form-control is-invalid',
             'id': 'name_of_client'
             }),
            'second_name_of_client': TextInput(attrs={
             'class': 'form-control is-invalid',
             'id': 'second_name_of_client'
             }),
            'phone_number_of_client': TextInput(attrs={
             'class': 'form-control is-invalid',
             'id': 'phone_number_of_client'
              }),
            'chooise_appointment_service': SelectMultiple(attrs={
             'class': 'form-control mr-sm-2 col-auto my-1',
             'id': 'chooise_appointment_service'
             }),
            'date_and_time_appointment': Select(attrs={
             'class': 'form-control mr-sm-2 col-auto my-1',
             'id': 'date_appointment'
             }),
        }
