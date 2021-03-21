from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages


def course(request):
  context = {
    "course": Course.objects.all()
  }
  return render(request, "index.html", context)

def new_course(request): #applies when hitting Add on main page
  #if request.method =="POST":
  newly_created_course = Course(name=request.POST['name'], description=request.POST['description'])
  newly_created_course.save()
 # return redirect(f"/course/{newly_created_course.id}")
  return redirect("/")

def destroy(request, id):
  context = {
    "course": Course.objects.get(id=id)
  }
  return render(request, "destroy.html", context)
 

def delete(request,id):  #applies when hitting Delete button on the main page
  if request.method =="POST":
    course = Course.objects.get(id=id)
    course.delete()
  return redirect("/")


