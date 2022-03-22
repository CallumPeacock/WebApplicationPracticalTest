from django.urls import path
from GAcourses import views

app_name = 'GAcourses'

urlpatterns = [
    path('', views.course, name='course')
]