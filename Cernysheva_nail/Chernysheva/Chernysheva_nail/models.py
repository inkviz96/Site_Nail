from django.db import models
from django.utils import timezone


# Create your models here.

#Appointment
class Appointment(models.Model):

    name_of_client = models.CharField(max_length=25, default='name', blank=False, null=True)
    second_name_of_client = models.CharField(max_length=30, default='None', blank=False, null=True)
    phone_number_of_client = models.CharField(max_length=10, blank=False, null=True)
    chooise_appointment_service = models.ManyToManyField('AppointmentChoiceService', related_name='choice_service')
    date_and_time_appointment = models.ManyToManyField('AppointmentChoiceDateAndTime', related_name='choice_date')
    date_appointment_create = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return '{}'.format(self.name_of_client)


class AppointmentChoiceService(models.Model):
    name_service = models.CharField(max_length=35, default='All')


    def __str__(self):
        return '{}'.format(self.name_service)

class AppointmentChoiceDateAndTime(models.Model):
    date_reception = models.CharField(max_length=35, default='All')


    def __str__(self):
        return '{}'.format(self.date_reception)



#Promotion
class Promotion(models.Model):
    title = models.CharField(max_length=25)
    body_promotion =  models.TextField(max_length=25, default='body_promotion')
    full_promotion =  models.TextField(max_length=250, default='full_promotion')
    image_promotion = models.URLField()

    def __str__(self):
        return '{}'.format(self.title)
