from django.views import View
from django.shortcuts import render,redirect
from models.models import Course


class CourseView(View):

    def get(self,request):
        courses = Course.objects.all()
        return render(request,'courses.html',{"data":courses})

class CourseDetailView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=course_id)
        return render(request,'each_course.html',{"object":course})

    def post(self,request,course_id):
        if request.method == "POST":
            rate=int(request.POST.get("rate"))
            course = Course.objects.get(id=course_id)
            new_rate=(course.rate*course.count + rate) / (course.count+1)
            course.count += 1
            course.rate = new_rate
            course.save()
            return redirect('course_list')
