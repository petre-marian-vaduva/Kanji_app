from django import forms
from django.forms import ModelForm #, TextInput, Textarea
from infrastructure.models import Instance,Server
from applications.models import ipm_appversions, lor_appversions
from scheduler.models import Runtime

class requestipmappupgradeform(ModelForm):
    class Meta:
        model = Runtime
        fields = ['instance_name','Server','Target_version']

    Target_version = forms.ModelChoiceField(queryset=ipm_appversions.objects.all().order_by('-id'),widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Application Version is Required'}) 
    instance_name = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A').filter(instance_name='iPM').order_by('instance_name'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Your Instance is Required'})
    Server = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Servers Required'})
																										  
class requestlorappupgradeform(ModelForm):
    class Meta:
        model = Runtime
        fields = ['instance_name','Server','Target_version']

    Target_version = forms.ModelChoiceField(queryset=lor_appversions.objects.all().order_by('-id'),widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Application Version is Required'}) 
    instance_name = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A').filter(instance_name='Lorenzo').exclude(instance_name__contains="NRPA").order_by('instance_name'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Your Instance is Required'})
    Server = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Servers Required'})
