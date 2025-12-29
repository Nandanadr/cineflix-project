from django import forms

from .models import Movie

import os

class MovieForm(forms.ModelForm):

    class Meta:

        model = Movie

        # fields = ['name','photo',]

        # fields = '__all__'

        exclude = ['uuid','active_status']

        widgets ={
            
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Movie name'}),

            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Movie description','row':3}),

            'release_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'industry':forms.Select(attrs={'class':'form-select'}),

            'runtime':forms.TimeInput(attrs={'class':'form-control','type':'time'}),

            'certification':forms.Select(attrs={'class':'form-select'}),

            'genre':forms.SelectMultiple(attrs={'class':'form-select'}),

            'artists':forms.SelectMultiple(attrs={'class':'form-select'}),

            'video':forms.TextInput(attrs={'class':'form-control','type':'url','placeholder':'Enter video url'}),

            'tags':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Movie tags','row':3}),

            'languages':forms.SelectMultiple(attrs={'class':'form-select'})

        }
        
    def clean(self):

        cleaned_data = super().clean()

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3*1024*1024:

            self.add_error('photo','maximum file size up 3MB')

    


