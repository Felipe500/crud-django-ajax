from .models import Client
from django import forms
from datetime import datetime


class ClientForm(forms.ModelForm):
    name = forms.CharField(required=False,
                           label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(required=False,
                              label='Sobrenome',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    date_birth = forms.DateField(initial=datetime.now(),
                                 label='Data de Nascimento',
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))
    cell_phone = forms.CharField(required=False,
                                 label='Celular',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=False,
                            label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    zip_code = forms.CharField(required=False,
                               label='CEP',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False,
                              label='Endereço',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        if not self.cleaned_data['is_active']:
            print('is_active ok')
            self.cleaned_data['is_active'] = True
        if not self.cleaned_data['name']:
            raise forms.ValidationError({'nome': "Por favor digite seu nome!"})
        return super().clean()

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = Client
        fields = '__all__'


class ClientReadOnlyForm(forms.ModelForm):
    name = forms.CharField(required=False,
                           label='Nome',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'readonly': 'readonly'}))
    surname = forms.CharField(required=False,
                              label='Sobrenome',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'readonly': 'readonly'}))

    date_birth = forms.DateField(initial=datetime.now(),
                                 label='Data de Nascimento',
                                 widget=forms.DateInput(attrs={'class': 'form-control',
                                                               'readonly': 'readonly'}))
    cell_phone = forms.CharField(required=False,
                                 label='Celular',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'readonly': 'readonly'}))
    email = forms.CharField(required=False,
                            label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'type': 'email',
                                                          'readonly': 'readonly'}))
    zip_code = forms.CharField(required=False,
                               label='CEP',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'readonly': 'readonly'}))
    address = forms.CharField(required=False,
                              label='Endereço',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'readonly': 'readonly'}))

    class Meta:
        model = Client
        fields = '__all__'

