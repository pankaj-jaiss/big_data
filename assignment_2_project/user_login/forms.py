from django import forms 

class Migration1Form(forms.Form):
    source = forms.CharField() 
    user = forms.CharField() 
    passwd = forms.CharField(required=False) 
    host = forms.CharField() 
    port = forms.IntegerField() 
    service_name = forms.CharField() 
    