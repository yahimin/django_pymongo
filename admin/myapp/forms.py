from django import forms
from django.core.validators import RegexValidator

class UserField(forms.Form):
    common_name =forms.CharField(label='common_name')
    category = forms.CharField(label="category")
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args , **kwargs)
    #     self.helper.form_method = 'post'
        
        
