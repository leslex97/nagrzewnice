from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import Device 
from devices.forms import SearchForm




class DevicesListView(FormView):
    template_name = 'devices_list.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["devices"] = Device.objects.all()
        
        return context
    
    def form_valid(self, form):
        
        query_set_filter = Q(
            Q(name__icontains=form.cleaned_data["fraze"])
            | Q(iP__icontains=form.cleaned_data["fraze"]))
        if form.cleaned_data["switches"]:
            query_set_filter &= Q(switch=form.cleaned_data["switches"])
        if form.cleaned_data["type_of_device"]:
            query_set_filter &= Q(type=form.cleaned_data["type_of_device"])
        
        return render(
            request=self.request,
            template_name=self.template_name,
            context={
             "form": form,
               "devices": Device.objects.filter(query_set_filter)})

class DeviceDetailsView(TemplateView):
    template_name = "device_details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["device"] = Device.objects.get(pk=self.kwargs["device_id"])
        return context




    
