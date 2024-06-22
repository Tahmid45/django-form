from django import forms
from django.core import validators
# widgets == field to html input  

# class contactForm(forms.Form):
#     name = forms.CharField(label='Full Name:', initial = 'Rahim', help_text="Total character must be within 70", required = False, disabled = True, widget = forms.Textarea(attrs = {'id':'textarea', 'class':'class1 class 2', 'placeholder' : 'Enter your Nmae'}))
#     file = forms.FileField()
#     email = forms.EmailField(label = 'User Email')
#     # age = forms.IntegerField()
#     # weight = forms.FloatField()
#     # balance = forms.DecimalField()
#     age = forms.CharField(widget = forms.NumberInput)
#     birthday = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))
#     appoinment = forms.DateTimeField(widget = forms.DateInput(attrs = {'type':'datetime-local'}))
#     CHOICES= [('s','small'), ('M','Medium'), ('L','Large')]
#     size = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
#     MEAL = [('p', 'Pepperoni'), ('M', 'Mashroom'),('B','Beef')]
#     pizza = forms.MultipleChoiceField(choices = MEAL, widget = forms.CheckboxSelectMultiple)


# class Student_Data(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget = forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data["name"]
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 character")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data["email"]
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your Email must contain .com")
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 character")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your Email must contain .com")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters")
        
class Student_Data(forms.Form):
    name = forms.CharField(widget = forms.TextInput, validators=[validators.MaxLengthValidator(10, message = 'enter a valid name with at least 10 characters')])
    
    text = forms.CharField(widget = forms.TextInput, validators = [len_check])

    email = forms.CharField(widget = forms.EmailInput, validators = [validators.EmailValidator(message = 'Enter a valid email')])
    
    age = forms.IntegerField(validators = [validators.MaxValueValidator(34, message = "age must be maximum 34"), validators.MinValueValidator(24, message="age must be at least 24")])

    file = forms.FileField(validators = [validators.FileExtensionValidator(allowed_extensions = ['pdf','jpg'], message = 'File extension must be ended with .pdf')])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_repass = self.cleaned_data['re_password']
        val_name = self.cleaned_data['name']

        if val_pass !=  val_repass:
            raise forms.ValidationError("Password doesn't match")

        if len(val_name) < 10:
            raise forms.ValodationError("Name must be less than 10 characters")
