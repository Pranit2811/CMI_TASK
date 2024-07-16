from django import forms
from .models import Company
from django.contrib.auth.models import User



class CompanyFilterForm(forms.Form):
        industry = forms.ChoiceField(
        choices=[('', 'All')] + [(industry, industry) for industry in Company.objects.values_list('industry', flat=True).distinct()],
        required=False
    )
        year_founded = forms.ChoiceField(
        choices=[('', 'All')] + [(year, year) for year in Company.objects.values_list('year_founded', flat=True).distinct()],
        required=False
    )
        country = forms.ChoiceField(
        choices=[('', 'All')] + [(country, country) for country in Company.objects.values_list('country', flat=True).distinct()],
        required=False
    )
        state = forms.ChoiceField(
        choices=[('', 'All')] + [(state, state) for state in Company.objects.values_list('locality', flat=True).distinct()],
        required=False
    )
        employees_from = forms.ChoiceField(required=False,
        choices=[('', 'All')] + [(employees_from, employees_from) for employees_from in Company.objects.values_list('total_employee_estimate', flat=True).distinct()],                                
    )
        employees_to = forms.ChoiceField(required=False,
                choices=[('', 'All')] + [(employees_to, employees_to) for employees_to in Company.objects.values_list('current_employee_estimate', flat=True).distinct()],                                
    )
        city = forms.ChoiceField(
        choices=[('', 'All')] + [(city, city) for city in Company.objects.values_list('locality', flat=True).distinct()],
        required=False
    )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }