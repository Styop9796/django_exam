from django.urls import path
from models.api.course import CourseView,CourseDetailView

urlpatterns = [
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_by_id'),
    path('', CourseView.as_view(), name='course_list'),
]