from django import forms
from .models import Video




class CommercialVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']  # Ensure these match your model's fields


#class AppointmentForm(forms.ModelForm):
 #   class Meta:
  #      model = Appointment
   #     fields = ['first_name', 'last_name', 'email', 'phone', 'request']