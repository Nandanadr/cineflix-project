from django import forms

from . models import SubscriptionPlans

import os

class SubscriptionplansForm(forms.ModelForm):

    class Meta:

        model = SubscriptionPlans

        exclude = ['uuid','active_status']

        widgets ={

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter subscriptionplans'}),

            'amount':forms.NumberInput(attrs={'class':'form-control'}),

            'devices':forms.SelectMultiple(attrs={'class':'form-select'}),

            'quality':forms.Select(attrs={'class':'form-select'}),

            'no_of_screens':forms.Select(attrs={'class':'form-select'}),

            'download_devices':forms.Select(attrs={'class':'form-select'})





        }