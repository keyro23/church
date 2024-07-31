# myapp/urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from .views import *


urlpatterns = [
    path("", views.index, name="home"),
    path('admin/', admin.site.urls),
    path('media-team/', views.media_team, name='media_team'),
   # path('book-service/', views.book_service, name='book_service'),
   # path('upload-commercial/', views.upload_commercial, name='upload_commercial'),
   # path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
   # path('videos/', views.video_list, name='video_list'),
   # path("appointment/", AppointmentTemplateView.as_view(), name="appointment"),
   # path("manage/", ManageAppointmentTemplateView.as_view(), name="manage"),
   # path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
   # path('process/<int:appointment_id>/<str:action>/', views.process_appointment, name='process_appointment'),
] 

