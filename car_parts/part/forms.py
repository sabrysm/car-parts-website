from django import forms
from .models import Part

INPUT_CLASSES = 'mt-2 px-3 py-2 border w-full outline-none border-solid border-[#c24235] rounded-lg font-light text-black'

class NewPartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('title', 'description', 'image', 'model', 'year', 'power', 'consumption', 'transmission', 'brand', 'condition', 'quantity',)
        help_texts = {
            'image': 'Upload an image of the part'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Battery',
                'name': 'title'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'With 2 fans, for bmw diesels',
                'default': 'With 2 fans, for bmw diesels',
                'rows':5, 
                'cols':20,
                'name': 'description'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'name': 'image'
            }),
                
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'BMW',
                'name': 'model'
            }),
            'year': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '2011',
                'name': 'year'
            }),
            'power': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '135kW',
                'name': 'power'
            }),
            'consumption': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Diesel',
                'name': 'consumption'
            }),
            'transmission': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Automatic/Manual',
                'name': 'transmission'
            }),
            'brand': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Vatra',
                'name': 'brand',
                'name': 'brand'
            }),
            'condition': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'New/Used',
                'name': 'condition'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'mt-2 px-3 py-2 border w-full outline-none border-solid border-[#c24235] rounded-lg font-light text-black',
                'placeholder': '1',
                'name': 'quantity'
            }),
        }

class SearchPartForm(forms.Form):
    # all the fields are optional
    model = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'BMW',
        'name': 'model'
    }))
    year = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': '2011',
        'name': 'year'
    }))
    power = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': '135kW',
        'name': 'power'
    }))
    consumption = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Diesel',
        'name': 'consumption'
    }))
    transmission = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Automatic/Manual',
        'name': 'transmission'
    }))
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Battery',
        'name': 'title'
    }))
    brand = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Varta',
        'name': 'brand'
    }))
    condition = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'New/Used',
        'name': 'condition'
    }))