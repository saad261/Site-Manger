from django import forms
from django.forms import ModelForm
from .models import Team
from .models import Task
from .models import Location
from .models import Site

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = "__all__"
        labels = {
            'site_name'          : "",
            'address'            : "",
            'link'               : "",
            'site_image'         : "",
            'manager'            : "manager",
        }
        widgets = {
            'site_name'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'site_name'}),
            'address'            : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'address'}),
            'link'               : forms.URLInput(attrs={'class':'form-control', 'placeholder':' link'}),
            'site_image'         : forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder': 'site_image'}),
            #'manager'            : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'manager'}),
        }



class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
        labels = {
            'code'               : "",
            'area'               : "",
            'location'           : "",
            'additional'         : "",
            'site'               : "site",
        }
        widgets = {
            'code'               : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'code'}),
            'area'               : forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'area'}),
            'location'           : forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'location'}),
            'additional'         : forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'additional'}),
            #'site'               : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'site'}),
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        labels = {
            'task_name'            : "",
            'starting_date'        : "",
            'location'             : "location",
        }
        widgets = {
            'task_name'            : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'task_name'}),
            'starting_date'        : forms. DateInput(attrs={'class': 'form-control', 'placeholder': 'starting_date'}),
            #'location'             : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'location'}),
        }


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        #fields = ("name","phone_number")
        labels = {
            'name'                 : "",
            'phone_number'         : "",
            'email'                : "",
            'task'                 : "task",
        }
        widgets = {
            'name'                 : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'phone_number'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone_number'}),
            'email'                : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            #'task'                 : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'task'}),
        }

