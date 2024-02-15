from django.urls import path
from .import views


urlpatterns = [
    path('course_view/',views.course_view,name='course_view'),
    path('course_view/<int:id>/',views.course_view_id,name='course_view'),
       
]
