from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class contactForm(forms.Form):
    first_name = forms.CharField(initial='Your name')
    email = forms.EmailField(label = "User Email")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField( required = False,)
    message = forms.CharField(
	max_length = 10,)
    email_address = forms.EmailField( 
    label="Please enter your email address",)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    exam_day = forms.DateField(initial=datetime.date.today)
    your_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    multiple_colors_choice = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    checkbox_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    