from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  FormView,
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from classroom.forms import ContactForm
from .models import Teacher

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL ?
    success_url = reverse_lazy('classroom:thank_you')
    # what to do with form ?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
     # look for model_form.html (by default)
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")

class TeacherListView(ListView):
    # look for model_list.html (by default)
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
    # look for model_detail.html (by default)
    model = Teacher

class TeacherUpdateView(UpdateView):
    # SHARE model_form.html (by default)
    model = Teacher
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # look for model_confirm_delete.html (by default)
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')