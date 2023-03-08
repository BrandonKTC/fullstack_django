from django.urls import path
from .views import (HomeView,
                   ThankYouView,
                   ContactFormView,
                   TeacherCreateView,
                   TeacherUpdateView,
                   TeacherDeleteView,
                   TeacherListView,
                   TeacherDetailView)

app_name = 'classroom'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("thank_you/", ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_update/<int:pk>', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>', TeacherDeleteView.as_view()),
    path('list_teacher', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
]