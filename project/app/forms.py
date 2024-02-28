from django import forms


class SyudentRegistration(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter your name'}) # _ converted into space and first charector converted into Uppercase
    email = forms.EmailField(label='Your Email', label_suffix='?',initial='neeraj@gmail.com', required=False,disabled=True)
    contact = forms.CharField(help_text='limit 20 char')
    description = forms.CharField(widget=forms.Textarea)
    password = forms.CharField() # bydefalut required is True 


# form Core Arguments
# required=True, required=False
# leble="value"
# max_length = 10, min_length = 4,
# label="String",
# initial='what value you want initially'
# lebel_suffix=" ",lebel_suffix=":",lebel_suffix=" ? "
# disabled=True, disabled=False,
# FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
# favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
# favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

# form Common Fields
# CharField()
# CharField(widget=forms.Textarea(attrs={'rows':3}))
# CharField(widget=forms.Textarea)
# EmailField()
# BooleanField()
# DateField()
# DateField(widget=NumberInput(attrs={'type': 'date'}))
# DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
# DecimalField()
# ChoiceField()
# ModelChoiceField()
# model_choice = forms.ModelChoiceField(queryset = MyModel.objects.all(),initial = 0)

