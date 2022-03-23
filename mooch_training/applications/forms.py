from django import forms
from django.forms import ModelForm #, TextInput, Textarea
from infrastructure.models import Instance,Server
from applications.models import ipm_appversions, lor_appversions
from scheduler.models import Runtime

class requestipmappupgradeform(ModelForm):
    class Meta:
        model = Runtime
        fields = ['instance_name','Server','Target_version']
    class Media:
        js = ('js/lookup_server_from_instance.js',)
    Target_version = forms.ModelChoiceField(queryset=ipm_appversions.objects.all().order_by('-id'),widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Application Version is Required'}) 
    instance_name = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A').filter(Instance_type='iPM'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Your Instance is Required'})
    Server = forms.ModelChoiceField(queryset=Server.objects.all(), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Servers Required'})


class requestlorappupgradeform(ModelForm):
    class Meta:
        model = Runtime
        fields = ['instance_name','Server','Target_version']
    class Media:
        js = ('js/lookup_server_from_instance.js',) 

    Target_version = forms.ModelChoiceField(queryset=lor_appversions.objects.all().order_by('-id'),widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Application Version is Required'}) 
    instance_name = forms.ModelChoiceField(queryset=Instance.objects.filter(status__exact='A').filter(Instance_type='Lorenzo'), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Your Instance is Required'})
    Server = forms.ModelChoiceField(queryset=Server.objects.all(), widget=forms.Select(attrs={'class':'custom-select mb-2 mr-sm-2 mb-sm-0'}),error_messages={'required': 'Servers Required'})



