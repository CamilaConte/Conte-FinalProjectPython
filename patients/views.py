from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from patients.models import Patient
from patients.forms import SearchPatientsForm, CreatePatientForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Patients(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patients/patients.html"
    context_object_name = "patients"
    
    def get_queryset(self):
        last_name = self.request.GET.get("last_name", "")
        patients = self.model.objects.filter(last_name__icontains=last_name)
        return patients
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchPatientsForm()
        context["last_name"] = self.request.GET.get("last_name", "")
        return context

class CreatePatient(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = CreatePatientForm
    template_name = "patients/create.html"
    success_url = reverse_lazy("patients")

class DeletePatient(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "patients/delete.html"
    success_url = reverse_lazy("patients")

#TODO: pisar el formulatio de estas views con uno personalizado donde le pueda agregar el widget
class UpdatePatient(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "patients/update.html"
    success_url = reverse_lazy("patients")
    fields = ["name", "last_name", "phone_number", "birth_date", "last_xray", "observations"]
    
class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/detail.html"


    