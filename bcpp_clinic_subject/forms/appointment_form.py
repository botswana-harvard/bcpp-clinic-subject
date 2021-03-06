from django import forms

from edc_appointment.modelform_mixins import AppointmentFormMixin
from edc_appointment.models import Appointment


class AppointmentForm(AppointmentFormMixin, forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
