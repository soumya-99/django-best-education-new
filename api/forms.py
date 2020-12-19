from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import *


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscriptionForm
        fields = '__all__'

        labels = {
            'name': 'Full Name',
            'email': 'Email',
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='white'),
    #             Column('email', css_class='white'),
    #             css_class='form-row'
    #         ),
    #     )