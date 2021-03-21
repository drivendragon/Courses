from django.urls import path   
from . import views


urlpatterns = [
    path('', views.course),
    path('new_course', views.new_course),
    path('course/destroy/<int:id>', views.destroy),
    path('course/destroy/course/<int:id>/delete', views.delete)
]